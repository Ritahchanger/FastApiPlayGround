from sqlalchemy import Column,Integer,String,ForeignKey


from sqlalchemy.orm import relationship

from app.database import Base

class Lesson(Base):
    
    __tablename__="lessons"
    
    
    id = Column(Integer,primary_key=True,index=True)
    
    title = Column(String(100),nullable=False)
    
    
    subject_id = Column(Integer,ForeignKey('subjects.id'))
    
    teacher_id = Column(Integer,ForeignKey('teachers.id'))
    
    
    class_id = Column(Integer,ForeignKey('classess.id'))
    
    
    subject = relationship("Subject")
    
    teacher = relationship("Teacher")
    
    student_class = relationship("Class")