# Lagos Traffic Congestion Predictor

3MTT Capstone Project — predicts traffic congestion level (Low/Medium/High) 
on a Lagos route at a given time, using historical traffic pattern data.

## Live App
Try it here: https://lagos-traffic-app-ha6wbhwv3n3fn7srsfenyf.streamlit.app/

## How it works
- Trained on historical route + time + weather data
- Random Forest Classifier (scikit-learn), 92% accuracy
- Input: route, hour, day of week, rain, holiday
- Output: predicted congestion level + confidence breakdown

## Tech Stack
Python, pandas, scikit-learn, Streamlit
