from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session

from . import crud
from .database import Base,engine
from .dependencies import get_db
from . import schemas,model

Base.metadata.create_all(bind=engine)

app=FastAPI(title="Student Notes API")

@app.get("/")
def root():
    return {"message":"Student Notes API is running"}

@app.post("/students/",response_model=schemas.studentcreate,status_code=status.HTTP_201_CREATED)
def create_student(student:schemas.studentcreate,db:Session=Depends(get_db)):
    return crud.create_student(db,student)

@app.get(
    "/students/",
    response_model=list[schemas.studentResponse],
)
def get_student(db:Session=Depends(get_db)):
    return crud.get_students(db)

@app.get(
    "/students/{student_id}",response_model=schemas.studentResponse,
)
def get_student_id(student_id: int,db:Session=Depends(get_db),):
    student=crud.get_student_by_id(db,student_id)
    if not student:
        raise HTTPException(
            status_code=404,
            detail="student not found",
        )
    return student

@app.post(
    "/students/{student_id}/notes/",
    response_model=schemas.notecreate,
    status_code=status.HTTP_201_CREATED
)
def create_note(student_id:int,note:schemas.notecreate,db:Session=Depends(get_db)):
    student=crud.get_student_by_id(db,student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="student not found",
        )
    
    return crud.create_notes(db,student_id,note)

@app.get("/notes/",response_model=list[schemas.noteResponse],)
def get_note(db:Session=Depends(get_db)):
    return crud.get_notes(db)

@app.get(
    "/notes/{note_id}",
    response_model=schemas.noteResponse,
)
def get_note_by_id(
    note_id: int,
    db: Session = Depends(get_db),
):
    note = crud.get_note_by_id(db, note_id)

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found",
        )

    return note

@app.put("/notes/{note_id}",response_model=schemas.noteResponse,)
def update_notes(
    note_id:int,
    note_update:schemas.noteUpdate,
    db:Session=Depends(get_db),
):
    note = crud.update_note(db,note_id,note_update)

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not Found"
        )
    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id:int,db:Session=Depends(get_db),):
    note=crud.delete_note(db,note_id)

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )
    return {"message":"Note Deleted Succesfully"}