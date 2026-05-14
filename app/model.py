from sqlalchemy import Column,Integer,String,ForeignKey,Text
from sqlalchemy.orm import relationship

from .database import Base

class Student(Base):
    __tablename__="students"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)

    notes=relationship("Note",back_populates="student")

class Note(Base):
    __tablename__="notes"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    content=Column(Text,nullable=False)

    student_id=Column(Integer,ForeignKey("students.id"),nullable=False)

    student=relationship("Student",back_populates="notes")