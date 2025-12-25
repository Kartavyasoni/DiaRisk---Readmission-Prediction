# 📁 Data Directory (Local Storage Only)

This folder holds the project’s datasets.  
**Raw datasets are not stored in this public repository** to avoid privacy, licensing, and size issues.

### 📍 Data Sources
- UCI Machine Learning Repository → *Diabetic Readmission Dataset*
- Dataset description PDF provides clinical feature definitions.

### 🗂️ Folder Structure
data/
├── raw/ # original CSVs stored locally (not pushed to GitHub)
├── processed/ # cleaned & feature-engineered datasets
└── README.md # documentation only

csharp
Copy code

### 🔒 Git Ignore Settings
The following paths are intentionally excluded from version control:
data/raw/
data/processed/
*.csv
*.parquet