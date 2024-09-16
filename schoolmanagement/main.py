from fastapi import FastAPI
from app.routers import student, teacher, subject, class_, lesson

app = FastAPI()

# Include routers
app.include_router(student.router, prefix="/students", tags=["Students"])
app.include_router(teacher.router, prefix="/teachers", tags=["Teachers"])
app.include_router(subject.router, prefix="/subjects", tags=["Subjects"])
app.include_router(class_.router, prefix="/classes", tags=["Classes"])
app.include_router(lesson.router, prefix="/lessons", tags=["Lessons"])
