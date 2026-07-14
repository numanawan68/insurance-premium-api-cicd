print(">>> APP.PY LOADED <<<")
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.predicton_response import PredictionResponse
from model.predict import predict_output,model,Model_version

app = FastAPI()

@app.get("/")
def home():
    return {'message': 'Welcome to Insurance Premium!'}
# health check endpoint (machine readable)
@app.get('/health')
def health_check():
    return{
        "status": "ok",
        "version": Model_version,
        "model_loded" :model is not None,
    }
@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:

        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'response': prediction})

    except Exception as e:

        return JSONResponse(status_code=500, content=str(e))




