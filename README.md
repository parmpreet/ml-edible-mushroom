# A simple machine learning app for detecting edible mushrooms

## Introduction
This application uses the Mushroom Classification dataset from https://www.kaggle.com for detecting if the mushrooms are poisonous or edible. `pycaret` library is used to preprocess the data and train the model. The model training is done using a jupyter notebook.

FastAPI is used to server the model on the REST API.

## Technology stack
### Library and packages
- pycaret
- FastApi
- Pandas

### IDE
Visual Studio Code

## setup
Dependencies for running this application can be installed using the `requirements.txt` file.

`pip install -r requirements.txt`

## Train model
The model can be trained by running the jupyter notebook. Name of the notebook is `mushroom_detection_101.ipynb`

## Serve the model
The api for serving this model is implemented using FastAPI. FastAPI server can be started using the following command

`uvicorn main:app --reload`

## Acknowledgements
### Dataset: https://www.kaggle.com/uciml/mushroom-classification
### Pycaret: https://github.com/pycaret/pycaret

