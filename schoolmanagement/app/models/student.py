from pydantic import BaseModel

class StudentBase(BaseModel):
    
    name:str
    
    age:int
    
    class_id:int
    
class StudentCreate(StudentBase):
    
    pass


class Student(StudentBase):
    
    id:int
    
    class Config:
        
        orm_mode=True