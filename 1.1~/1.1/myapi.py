from fastapi import FastAPI

from typing import Optional

from pydantic import BaseModel


app = FastAPI()


students = {
    
    1:{
        "name":"John Murithi",
        "age":"17",
        "year":"Year 12",
    },
    2:{
        "name":"Eric Gratified",
        "age":"20",
        "year":"Year 14",
    },
    3:{
        "name":"Kelvin Mercelo",
        "age":"35",
        "year":"Year 35",
    },
    
}


BOOKS={
    
    1:{"title":"Title One","Author":"kelvin Oganda"},
    2:{"title":"Title two","Author":"kelvin Munyao"},
    3:{"title":"Title three","Author":"Ritah Hearts"},
    4:{"title":"Title four","Author":"MIlly Cent"},
    5:{"title":"Title five","Author":"Melvin Brourne"},
    6:{"title":"Title six","Author":"David carter"}

}

class Student(BaseModel):
    
    name:str
    
    age:int
    
    year:str
    
    

@app.get("/")

def index():
    
    return {"success":True,"status":200,"data":students}

@app.get("/get-students/{student_id}")

def get_student(student_id:int):
    
    if student_id not in students:
         
        raise HTTPException(status_code=404,detail="Student not found")
    
    return students[student_id]


@app.get("/get-by-name")

def get_student_by_name(name:Optional[str]=None):
    
    if name is None:
        
        raise HTTPException(status_code=400,detail="Name query parameter is required")
    
    for student_id, student_info in students.items():
        
        if student_info["name"] == name:
            
            return student_info
         
    raise HTTPException(status_code=404,detail="Student not found")

@app.get("/get-books")

def get_all_books():
    
    return {"success":True,"status":200,"data":BOOKS}


@app.get("/book-by-Title")

async def get_book_by_name(title:Optional[str]=None):
    
    if title is None:
        
        raise HTTPException(status_code=400,detail="Title parameter is required")
    
    for book_id,book_information in BOOKS.items():
        
        if book_information["title"].lower() ==title.lower():
            
            return book_information
        
    
    raise HTTPException(status_code=404,detail="Book not found")