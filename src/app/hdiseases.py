from pydantic import BaseModel,Field
# 2. Class which describes Hd measurements
class heartdisease(BaseModel):
    Age : int
    Sex: str
    RestingBP: int
    Cholesterol: int
    FastingBS: int
    MaxHR: int
    Oldpeak: float
    ASY: int
    ATA: int
    NAP: int
    TA: int
    LVH: int
    Normal: int
    ST: int
    N: int
    Y: int
    Down: int
    Flat: int
    Up: int
    