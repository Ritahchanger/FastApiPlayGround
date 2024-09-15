from sqlalchemy import Column,Integer,String


from sqlalchemy.orm import relationship


from app.database import Base

class Classess(Base):
    
    
    __tablename__="classes"
    
    id = Column(Integer,primary_key=True,index=True)
    
    
    name=Column(String(50),nullable=False)
    
    
    students = relationship("Student",back_populates="student_class")
    
    
    