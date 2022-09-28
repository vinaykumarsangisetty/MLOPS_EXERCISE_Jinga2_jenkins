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

# 2. Create the app object
app = FastAPI(
 title="SVM Model ML API With Connection to Azure MYSQL DB",
description="Heart Disease Prediction"
)
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



pickle_insert = open("heartdisease.pkl", "rb")
transformer = pickle.load(pickle_insert)

heart_disease=[]

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get("/frontend", response_class=HTMLResponse)
async def read_item(request: Request):
    Age = ''
    Sex = ''
    RestingBP= ''
    Cholesterol= ''
    FastingBS= ''
    MaxHR= ''
    Oldpeak= ''
    ASY= ''
    ATA= ''
    NAP= ''
    TA= ''
    LVH= ''
    Normal= ''
    ST= ''
    N= ''
    Y= ''
    Down= ''
    Flat= ''
    Up= ''
    HeartDisease = ''

return templates.TemplateResponse("index.html",context={'request': request, 'Age': Age,'Sex':Sex,'RestingBP':RestingBP,'Cholesterol':Cholesterol,'FastingBS':FastingBS,'MaxHR':MaxHR,'Oldpeak':Oldpeak, 'ASY': ASY,'ATA':ATA,'NAP':NAP,'TA':TA,'LVH':LVH,'Normal':Normal,'ST':ST,'N':N,'Y':Y,'Down':Down,'Flat':Flat,'Up':Up,'HeartDisease':HeartDisease})


@app.post("/frontend")
def form_post(request: Request, Age: int = Form(...),Sex:int=Form(...),RestingBP:int=Form(...),Cholesterol:int=Form(...),FastingBS:int=Form(...),MaxHR:int=Form(...), Oldpeak: int = Form(...),ASY:int=Form(...),ATA:int=Form(...),NAP:int=Form(...),TA:int=Form(...),LVH:int=Form(...), Normal: int = Form(...),ST:int=Form(...),N:int=Form(...),Y:int=Form(...),Down:int=Form(...),Flat:int=Form(...), Up: int = Form(...)):
    Age = Age
    Sex = Sex
    RestingBP= RestingBP
    Cholesterol= Cholesterol
    FastingBS= FastingBS
    MaxHR= MaxHR
    Oldpeak= Oldpeak
    ASY= ASY
    ATA= ATA
    NAP= NAP
    TA= TA
    LVH= LVH
    Normal= Normal
    ST= ST
    N= N
    Y= Y
    Down= Down
    Flat= Flat
    Up= Up
    
    testing_data = [[Age, Sex, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak, ASY, ATA, NAP, TA, LVH, Normal, ST, N, Y, Down, Flat, Up]]
    class_idx =predict(testing_data)
    prediction = class_idx


    return templates.TemplateResponse("index.html",context={'request': request, 'Age': Age,'Sex':Sex,'RestingBP':RestingBP,'Cholesterol':Cholesterol,'FastingBS':FastingBS,'MaxHR':MaxHR,'Oldpeak':Oldpeak, 'ASY': ASY,'ATA':ATA,'NAP':NAP,'TA':TA,'LVH':LVH,'Normal':Normal,'ST':ST,'N':N,'Y':Y,'Down':Down,'Flat':Flat,'Up':Up,'prediction':prediction})


@app.get('/')
def welcome():
    return {f'HOME PAGE Connected to MYSQL DB'}

@app.get('/{name}')
def get_name(name: str):
    return {'Welcome': f'{name}'}

@app.get('/predictions')
def prediction_table(db: Session = Depends(get_db)):
    predicted_hd = db.query(Models.heart_disease).all()
    return predicted_hd

@app.get('/predictions/{id}')
def prediction_table(id:int,db:Session=Depends(get_db)):
    predicted_hd=db.query(Models.heart_disease).filter(Models.heart_disease.id==id).first()
    if not predicted_hd:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id Not Found")
    return predicted_hd

@app.delete('/predictions/{id}')
def delete(id:int, hd: heartdisease,db:Session=Depends(get_db)):
    hd_model=db.query(Models.heart_disease).filter(Models.heart_disease.id==id).first()
    
    if hd_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {ID_HD} : Does Not Exist"
        )

    db.query(Models.heart_disease).filter(Models.heart_disease.id==id).delete()
    
    db.commit()
    return {f'Prediction with id:{id} deleted succesfully'}

@app.put('/predictions/{id}')
def updation(id:int,request:hdiseases.heartdisease,db:Session=Depends(get_db)):
    updation=db.query(Models.heart_disease).filter(Models.heart_disease.id==id)
    if not updation.first():
        pass
    updation.update(request.dict())
    db.commit()
    return{f'Succesfully updated id:{id}'}


# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence

@app.post('/predict',status_code=status.HTTP_201_CREATED)
def predict_HD(request: heartdisease, db: Session = Depends(get_db)):
    testing_data=[[
        request = Models.heart_disease()
        request.Age,
        request.Sex,
        request.RestingBP,
        request.Cholesterol,
        request.FastingBS,
        request.MaxHR,
        request.Oldpeak,
        request.ASY,
        request.ATA,
        request.NAP,
        request.TA,
        request.LVH,
        request.Normal,
        request.ST,
        request.N,
        request.Y,
        request.Down,
        request.Flat,
        request.Up
    ]]
    class_idx = predict(testing_data)
    request.prediction=class_idx
    
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


    
    return templates.TemplateResponse("index.html",context={'request': request, 'Age': Age,'Sex':Sex,'RestingBP':RestingBP,'Cholesterol':Cholesterol,'FastingBS':FastingBS,'MaxHR':MaxHR,'Oldpeak':Oldpeak, 'ASY': ASY,'ATA':ATA,'NAP':NAP,'TA':TA,'LVH':LVH,'Normal':Normal,'ST':ST,'N':N,'Y':Y,'Down':Down,'Flat':Flat,'Up':Up})
              
              

'''
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
    '''



# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)