# DPSChallenge

This repo for DPS challenge

## Data processing and visualization

Please find it in *data_processing.ipynb*

## Prediction
Featurization and model training is in *prediction.ipynb* (and *utils.py*)

Linear regression model is stored in *./Model/linear_reg.pkl*

## Deployment
Deployed at "http://dpschallenge-env.eba-mvnzkr95.us-east-1.elasticbeanstalk.com/predict", using aws Elastic Beanstalk


Request should be a JSON body like this:

```
{
    "category": "Fluchtunfälle",
    "type": "insgesamt",
    "year": 2022,
    "month": 11
}
```

(Keys can also be in German, case and order doesn't matter, but the four features must be all included and the values shouldn't be out of scope.)

Example return:

```
{
    "prediction": 1512.0035623286503
}
```
