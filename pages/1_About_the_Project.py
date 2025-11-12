import streamlit as st

st.markdown("<h1>📊 About the Project</h1>", unsafe_allow_html=True)
st.markdown("""
This project leverages **machine learning** — specifically the **XGBoost Regressor** — 
to predict diabetes risk using a combination of **clinical** and **lifestyle factors**.

### ⚙️ Model Highlights
- Algorithm: **XGBoost Regressor**
- R² Score: **0.9883**
- Tuned Parameters: `learning_rate`, `n_estimators`, `max_depth`, `subsample`
- Dataset: Synthetic but clinically structured health data
- Evaluation Metric: R², RMSE

### 🧠 Core Idea
By analyzing correlations between features such as glucose levels, BMI, HbA1c, 
and blood pressure, the model can output a **quantitative risk score (0–30)** 
that represents the probability of developing diabetes.

### 🔬 Why XGBoost?
XGBoost was chosen for its:
- Superior handling of **non-linear relationships**
- **Regularization** to prevent overfitting
- **Fast computation** and robust ensemble structure

### 🩺 Impact
With such models, hospitals and clinics can implement **early screening tools** 
to identify at-risk individuals and personalize interventions — potentially 
reducing the prevalence and burden of diabetes globally.
""")
