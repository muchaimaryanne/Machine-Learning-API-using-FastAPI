from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Sepsis(BaseModel):
    Plasmaglucose:float
    BloodWorkResult1:float
    BloodPressure:float
    BloodWorkResult2:float
    BloodWorkResult3: float
    Bodymassindex: float
    BloodWorkResult4: float
    Age: float
    

    