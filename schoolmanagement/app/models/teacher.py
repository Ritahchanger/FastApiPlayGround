from sqlalchemy import Column,Integer,String


from app.database import Base


class Teacher(Base):
    
    
    __tablename__="teachers"
    
    id = Column(Integer,primary_key=True,index=True)
    
    name = Column(String(50),nullable=False)
    
    subject_id = Column(Integer)