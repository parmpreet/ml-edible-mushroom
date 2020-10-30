from typing import Optional

from fastapi import FastAPI, Form
import pandas
from pydantic import BaseModel

from pycaret.classification import load_model, predict_model
import pandas as pd

class Mushroom(BaseModel):
    cap_shape: Optional[str] = None
    cap_surface: Optional[str] = None
    cap_color: Optional[str] = None
    bruises: Optional[str] = None
    odor:Optional[str] = None
    gill_attachment: Optional[str] = None
    gill_spacing: Optional[str] = None
    gill_size:Optional[str] = None
    gill_color:Optional[str] = None
    stalk_shape: Optional[str] = None
    stalk_root:Optional[str] = None
    stalk_surface_above_ring: Optional[str] = None
    stalk_surface_below_ring: Optional[str] = None
    stalk_color_above_ring: Optional[str] = None
    stalk_color_below_ring: Optional[str] = None
    veil_type: Optional[str] = None
    veil_color: Optional[str] = None
    ring_number: Optional[str] = None
    ring_type: Optional[str] = None
    spore_print_color: Optional[str] = None
    population: Optional[str] = None
    habitat: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "cap-shape": [self.cap_shape],
            "cap-surface": [self.cap_surface],
            "cap-color": [self.cap_color],
            "bruises": [self.bruises],
            "odor": [self.odor],
            "gill-attachment": [self.gill_attachment],
            "gill-spacing": [self.gill_spacing],
            "gill-size": [self.gill_size],
            "gill-color": [self.gill_color],
            "stalk-shape": [self.stalk_shape],
            "stalk-root": [self.stalk_root],
            "stalk-surface-above-ring": [self.stalk_surface_above_ring],
            "stalk-surface-below-ring": [self.stalk_surface_below_ring],
            "stalk-color-above-ring": [self.stalk_color_above_ring],
            "stalk-color-below-ring": [self.stalk_color_below_ring],
            "veil-type": [self.veil_type],
            "veil-color": [self.veil_color],
            "ring-number": [self.ring_number],
            "ring-type": [self.ring_type],
            "spore-print-color": [self.spore_print_color],
            "population": [self.population],
            "habitat": [self.population]
        }

app = FastAPI()
model = load_model("final_knn_30-10-2020")
# TODO: load the config to setup app
@app.on_event("startup")
def startup():
    """
    This method will load the model on startup
    """
    # model =
# TODO: Return the useful status information
@app.get("/")
def read_root():
    """
    This method returns the status of the app
    """
    return {'status': True}

@app.post('/detect')
def detect(mushroom: Mushroom):
    data = pd.DataFrame(mushroom.to_dict())
    prediction = predict_model(model, data)
    # print(prediction)
    return make_human_readable(prediction)


def make_human_readable(data: pandas.DataFrame) -> dict:
    return {
        "prediction": "Poisonous" if data.iloc[0]['Label'] == "p" else "Edible",
        "confidence": data.iloc[0]['Score']
    }
