# 🚑 DiaRisk: Clinical Readmission Prediction & Cost Containment Engine

**Objective:** Predict 30-day readmission risk for diabetic patients and estimate financial impact of preventive interventions.

### 📌 Why This Project Matters
Hospitals lose millions in CMS penalties due to readmissions. DiaRisk identifies high-risk patients *before discharge*, enabling early intervention and improving outcomes.

### 📊 Key Features
- 📦 End-to-end ETL Pipeline (Pandas + SQL-style preprocessing)
- 🤖 XGBoost readmission classifier (Current AUC: **0.83**)
- 💡 Cost Impact Simulator — models potential savings up to **$2M+/year**
- 📈 Clinician-friendly risk dashboard (Tableau / Streamlit)

### 🛠️ Tech Stack
`Python, Pandas, Scikit-Learn, XGBoost, SHAP, Streamlit, Tableau`

---

## 🚧 Project Architecture (Working Plan)

Raw Data → ETL → Feature Store → ML Model → Risk Scoring API → Dashboard

## 📂 Repository Structure

├── data/
├── notebooks/
├── src/
├── models/
├── dashboard/
└── reports/

---

## 📆 Project Roadmap (Current Phase)
- [x] Repo setup & structure
- [ ] Dataset EDA & Data Quality Report
- [ ] ETL + Feature Engineering Pipeline
- [ ] XGBoost Model Training + SHAP Explainability
- [ ] ROI Cost Impact Simulation
- [ ] Streamlit Web App Deployment

---

## 📜 License
MIT License — Free to use & modify.

---

## 🤝 Contributions
Pull requests welcome — feedback appreciated!