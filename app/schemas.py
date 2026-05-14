from pydantic import BaseModel , EmailStr


class studentcreate(BaseModel):
    name:str
    email:EmailStr

class studentResponse(BaseModel):
    id:int
    name:str
    email:EmailStr

    class Config:
        from_attributes =True

class notecreate(BaseModel):
    title:str
    content:str

class noteUpdate(BaseModel):
    title:str
    content:str

class noteResponse(BaseModel):
    id:int
    title:str
    content:str
    student_id:int

    class Config:
        from_attribute=True