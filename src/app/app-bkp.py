# 1. Library imports
import uvicorn
from fastapi import FastAPI, Depends,HTTPException,Form

from hdiseases import heartdisease
import numpy as np
import pickle
import json
import joblib
import numpy as np
import Models
import pandas as pd
from Database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.params import Depends

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


Models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# 2. Create the app object
app = FastAPI()

pickle_insert = open("heartdisease.pkl", "rb")
transformer = pickle.load(pickle_insert)



heart_disease=[]

# 3. Index route, opens automatically on http://127.0.0.1:6000

@app.get('/')
def index(db: Session = Depends(get_db)):
    return db.query(Models.heart_disease).all()


@app.get('/{name}')
def get_name(name: str):
    return {'Welcome': f'{name}'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:6000/AnyNameHere

@app.delete('/{ID_HD}')
def delete_note(ID_HD:int, hd: heartdisease, db: Session = Depends(get_db)):

    hd_model=db.query(Models.heart_disease).filter(Models.heart_disease.id==ID_HD).first()

    if hd_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {ID_HD} : Does Not Exist"
        )

    db.query(Models.heart_disease).filter(Models.heart_disease.id==ID_HD).delete()
    db.commit()


# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_HD(hd: heartdisease, db: Session = Depends(get_db)):

    hd_model = Models.heart_disease()
    hd_model.Age = hd.Age
    hd_model.Sex = hd.Sex
    hd_model.RestingBP = hd.RestingBP
    hd_model.Cholesterol = hd.Cholesterol
    hd_model.FastingBS = hd.FastingBS
    hd_model.MaxHR = hd.MaxHR
    hd_model.Oldpeak = hd.Oldpeak
    hd_model.ASY = hd.ASY
    hd_model.ATA = hd.ATA
    hd_model.NAP = hd.NAP
    hd_model.TA = hd.TA
    hd_model.LVH = hd.LVH
    hd_model.Normal = hd.Normal
    hd_model.ST = hd.ST
    hd_model.N = hd.N
    hd_model.Y = hd.Y
    hd_model.Down = hd.Down
    hd_model.Flat = hd.Flat
    hd_model.Up = hd.Up

    data = hd.dict()
    Age = data['Age']
    Sex = data['Sex']
    RestingBP= data['RestingBP']
    Cholesterol= data['Cholesterol']
    FastingBS= data['FastingBS']
    MaxHR= data['MaxHR']
    Oldpeak= data['Oldpeak']
    ASY= data['ASY']
    ATA= data['ATA']
    NAP= data['NAP']
    TA= data['TA']
    LVH= data['LVH']
    Normal= data['Normal']
    ST= data['ST']
    N= data['N']
    Y= data['Y']
    Down= data['Down']
    Flat= data['Flat']
    Up= data['Up']


    
    HeartDisease = transformer.predict([[Age, Sex, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak, ASY, ATA, NAP, TA, LVH, Normal, ST, N, Y, Down, Flat, Up]])


    print(HeartDisease)
    print(HeartDisease[0])
    
    if (HeartDisease[0] > 0.5):
        HeartDisease = "Heart Disease Identified"
        hd_model.HeartDisease = 1
        hd_model.prediction = "Heart Disease Identified"
        
    else:
        HeartDisease = "No Heart Disease"
        hd_model.HeartDisease = 0
        hd_model.prediction = "No Heart Disease"
#     model_finalprediction=Models.heart_disease(hd_model, HeartDisease=hd.HeartDisease)
    db.add(hd_model)
    db.commit()

    return {
        'HeartDisease': HeartDisease
    }




# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)