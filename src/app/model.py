from sqlalchemy import Column,Float,String,Integer
from .database import Base
class heart_disease(Base):
    __tablename__='heart_disease_prediction'
    id=Column(Integer,primary_key=True,index=True)
    Age =Column(Integer)
    Sex= Column(String)
    ChestPainType= Column(String)
    RestingBP=Column(Integer)
    Cholesterol=Column(Integer)
    FastingBS=Column(Integer)
    RestingECG=Column(String)
    MaxHR=Column(Integer)
    ExerciseAngina=Column(String)
    Oldpeak=Column(Float)
    ST_Slope=Column(String)
    HeartDisease=Column(Integer)