from sqlalchemy import Column,Integer,String


from app.database import Base

class Subject(Base):
    
    __tablename__="subjects"
    
    
    id = Column(Integer,primary_key=True,index=True)
    
    
    name = Column(String(50),nullable=False)
    
    
    