import streamlit as st

st.set_page_config(page_title="Thyroid Predictor", layout="centered")
st.title("🧠 Thyroid Condition Predictor")
st.write("Please fill out the form to check the chances of thyroid conditions.")

# Basic Info
st.header("👤 Basic Info")
height = st.number_input("Height (in cm)", min_value=50, max_value=250)
weight = st.number_input("Weight (in kg)", min_value=20, max_value=300)
weight_change = st.radio(
    "Have you experienced significant weight change?",
    ("No change", "Weight Gain", "Weight Loss")
)

# Symptom Checker
st.header("🩺 Symptom Checker")

# Hypothyroid Symptoms
sweating = st.checkbox("Reduced Sweating")
obesity = st.checkbox("Obesity / Unexplained Weight Gain")
fatigue = st.checkbox("Fatigue")
cold_intolerance = st.checkbox("Cold Intolerance")
dry_skin = st.checkbox("Dry Skin")
constipation = st.checkbox("Constipation")
irregular_cycle = st.checkbox("Irregular Periods")

# Hyperthyroid Symptom
weight_loss = st.checkbox("Unexplained Weight Loss")
heat_intolerance = st.checkbox("Heat Intolerance")
anxiety = st.checkbox("Anxiety / Nervousness")


# Button to Predict
if st.button("🔍 Predict Thyroid Condition"):

    # Count symptoms
    hypo_symptoms = [sweating, obesity, fatigue, cold_intolerance, dry_skin, constipation, irregular_cycle]
    hyper_symptoms = [weight_loss, heat_intolerance, anxiety, irregular_cycle]

    hypo_score = sum(hypo_symptoms)
    hyper_score = sum(hyper_symptoms)

    # Convert to percentage
    hypo_percent = int((hypo_score / len(hypo_symptoms)) * 100)
    hyper_percent = int((hyper_score / len(hyper_symptoms)) * 100)

    # Show percentages
    st.subheader("📊 Prediction Result")
    
    if hypo_percent > hyper_percent:
        st.progress(hypo_percent)
        st.info(f"**Hypothyroidism Chances:** {hypo_percent}%")
    elif hyper_percent > hypo_percent:
        st.progress(hyper_percent)
        st.info(f"**Hyperthyroidism Chances:** {hyper_percent}%")
    else:
        st.progress(hypo_percent)
        st.info(f"**Both Hypo- and Hyperthyroidism Chances:** {hypo_percent}%")


    # Final suggestion
    if hypo_percent > hyper_percent and hypo_percent >= 50:
        st.warning("🔎 You may have signs of **Hypothyroidism**. Please consult a doctor.")
    elif hyper_percent > hypo_percent and hyper_percent >= 50:
        st.warning("🔎 You may have signs of **Hyperthyroidism**. Please consult a doctor.")
    else:
        st.success("✅ No strong signs of thyroid issues detected.")


