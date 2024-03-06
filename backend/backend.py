from fastapi import FastAPI
import pandas as pd
import os 


current_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_dir, "..", "data", "North America Restaurants.csv")
print(data_file)
df = pd.read_csv(data_file)
app = FastAPI()

@app.get('/')
def index():
    return {"Hello": "world"}


@app.get('/show')
def showData():
    return df.to_json()
