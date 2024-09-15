from fastapi import FastAPI

from typing import Optional

app = FastAPI()


students = {
    
    1:{
        "name":"John Murithi",
        "age":"17",
        "class":"Year 12",
    },
    2:{
        "name":"Eric Gratified",
        "age":"20",
        "class":"Year 14",
    },
    3:{
        "name":"Kelvin Mercelo",
        "age":"35",
        "class":"Year 35",
    },
    
}

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
