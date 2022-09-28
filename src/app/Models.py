from sqlalchemy import Column,Integer, Float, String
from Database import Base

class heart_disease(Base):
    __tablename__='heart_disease_prediction'
    id=Column(Integer,primary_key=True,index=True)
    Age =Column(Integer)
    Sex= Column(String(10))
    RestingBP= Column(Integer)
    Cholesterol=Column(Integer)
    FastingBS=Column(Integer)
    MaxHR=Column(Integer)
    Oldpeak=Column(Float)
    ASY=Column(Integer)
    ATA=Column(Integer)
    NAP=Column(Integer)
    TA=Column(Integer)
    LVH=Column(Integer)
    Normal=Column(Integer)
    ST=Column(Integer)
    N=Column(Integer)
    Y=Column(Integer)
    Down=Column(Integer)
    Flat=Column(Integer)
    Up=Column(Integer)
    HeartDisease=Column(Integer)
    prediction=Column(String(40))