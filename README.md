# Lagos Traffic Congestion Predictor

3MTT Capstone Project — predicts traffic congestion level (Low/Medium/High) 
on a Lagos route at a given time, using historical traffic pattern data.

## Live App
Try it here: [add your Streamlit link here once deployed]

## How it works
- Trained on historical route + time + weather data
- Random Forest Classifier (scikit-learn), 92% accuracy
- Input: route, hour, day of week, rain, holiday
- Output: predicted congestion level + confidence breakdown

## Tech Stack
Python, pandas, scikit-learn, Streamlit
