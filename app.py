from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from summarylm.pipeline.prediction import PredictionPipeline
from summarylm.exception import CustomException

text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url='/docs')

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Successful!!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")
    
@app.post("/predict")
async def predict_route(text, max_length: int = 128):
    try:
        print(type(max_length))
        obj = PredictionPipeline()
        text = obj.predict(text, max_length)
        return text
    except Exception as e:
        raise CustomException(e, sys) from e
    