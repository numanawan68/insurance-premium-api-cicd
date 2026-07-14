import pickle
import pandas as pd
from pandas import DataFrame

# import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

#MLflow Like software where we get
Model_version = '1.0.0'

#get classes labels from model(important for matching probability to class name)
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])
    predicted_class =model.predict(df)[0]

    #get probabilities for all classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)
    #create mapping
    class_probs = dict (zip(class_labels, map(lambda x: round(x, 2), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence,4),
        "class_probs": class_probs
    }


