# 1. Library imports
import uvicorn
from fastapi import FastAPI
from sepsis import Sepsis
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("pipeline.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome the Sepssis prediction model': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_sepssis(data:Sepsis):
    data = data.dict()
    PRG=data['PRG']
    PL=data['PL']
    PR=data['PR']
    SK=data['SK']
    TS=data['TS']
    M11=data['M11']
    BD2=data['BD2']
    Age=data['Age']
    Insurance=data['Insurance']
     
    
    
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[PRG,PL,PR,SK,TS,M11,BD2,Age,Insurance]])
    if(prediction[0]>0.5):
        prediction="Sepssis present"
    else:
        prediction="Sepssis Absent"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload