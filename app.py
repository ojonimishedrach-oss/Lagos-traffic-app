import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Lagos Traffic Congestion Predictor", page_icon="🚦", layout="centered")

@st.cache_resource
def load_model():
    model = joblib.load("congestion_model.pkl")
    route_encoder = joblib.load("route_encoder.pkl")
    return model, route_encoder

model, route_encoder = load_model()

st.title("🚦 Lagos Traffic Congestion Predictor")
st.write("Predict congestion level on a Lagos route for a given day and time.")

st.divider()

# ---- Inputs ----
route = st.selectbox("Route", sorted(route_encoder.classes_))

col1, col2 = st.columns(2)
with col1:
    hour = st.slider("Hour of day (24h)", 0, 23, 8)
with col2:
    day_name = st.selectbox(
        "Day of week",
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    )

col3, col4 = st.columns(2)
with col3:
    is_raining = st.checkbox("Raining")
with col4:
    is_holiday = st.checkbox("Public holiday")

day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(day_name)

# ---- Predict ----
if st.button("Predict Congestion", type="primary"):
    is_weekend = 1 if day_of_week >= 5 else 0
    is_rush_hour = 1 if (7 <= hour <= 9 or 16 <= hour <= 19) else 0
    route_encoded = route_encoder.transform([route])[0]

    input_df = pd.DataFrame([{
        "route_encoded": route_encoded,
        "hour": hour,
        "day_of_week": day_of_week,
        "is_weekend": is_weekend,
        "is_rush_hour": is_rush_hour,
        "is_raining": int(is_raining),
        "is_holiday": int(is_holiday)
    }])

    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]
    prob_dict = dict(zip(model.classes_, probabilities))

    st.divider()

    color_map = {"Low": "green", "Medium": "orange", "High": "red"}
    st.markdown(f"### Predicted Congestion: :{color_map[prediction]}[{prediction}]")

    st.write("**Confidence breakdown:**")
    for level in ["Low", "Medium", "High"]:
        st.progress(float(prob_dict.get(level, 0)), text=f"{level}: {prob_dict.get(level, 0)*100:.1f}%")

st.divider()
st.caption("3MTT Capstone Project by Idris Shedrach Ojonimi — Traffic Congestion Predictor for Lagos Commuters")
