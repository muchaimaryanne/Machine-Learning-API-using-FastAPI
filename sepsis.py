from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Sepsis(BaseModel):
    PRG: float 
    PL: float 
    PR: float 
    SK: float
    TS: float
    M11: float
    BD2: float
    Age: float
    Insurance: float