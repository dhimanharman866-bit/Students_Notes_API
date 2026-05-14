from sqlalchemy.orm import Session

from . import model
from . import schemas

def create_student(db:Session,student:schemas.studentcreate):

    db_student=model.Student(**student.model_dump())

    db.add(db_student)

    db.commit()

    db.refresh(db_student)

    return db_student

def get_students(db:Session):
    return db.query(model.Student).all()

def get_student_by_id(db:Session,student_id:int):
    return (
        db.query(model.Student).filter(model.Student.id==student_id).first()
    )

def create_notes(db:Session,student_id:int,note:schemas.notecreate):
    db_note=model.Note(
        title=note.title,
        content=note.content,
        student_id=student_id,
    )

    db.add(db_note)

    db.commit()

    db.refresh(db_note)

    return db_note

def get_notes(db:Session):
    return db.query(model.Note).all()


def get_note_by_id(db:Session,note_id:int):
    return (
        db.query(model.Note).filter(model.Note.id==note_id).first()
    )

def update_note(
        db:Session,
        note_id:int,
        note_update:schemas.noteUpdate,
):
    db_note=get_note_by_id(db,note_id)

    if not db_note:
        return None
    
    db_note.title=note_update.title
    db_note.content=note_update.content

    db.commit()

    db.refresh(db_note)

    return db_note

def delete_note(db:Session,note_id:int):
    db_note=get_note_by_id(db,note_id)

    if not db_note:
        return None
    
    db.delete(db_note)

    db.commit()

    return db_note