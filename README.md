
# 📊 Academic Performance Analyser – Streamlit Dashboard

This is a **Streamlit-based dashboard** that visualizes academic performance (CPI/SPI) for students using anonymized data from IIT Kanpur. It allows users to search for any student by **roll number or name**, view their **CPI for the last 4 semesters**, and compare performance within their **department and institute**.

---

## 🚀 Features

- 📌 Search student by **roll number or name**
- 📈 Display **CPI across 4 semesters**
- 🥇 Show **Department Rank** and **Institute Rank**
- 📊 Plot **CPI trend** along with:
  - Department Average
  - Department Topper
- 🔍 Compare CPI of **two students side-by-side**

---

## 🛠️ How to Run the Project

### ✅ Step 1: Clone the repository

```bash
git clone https://github.com/your-username/academic-performance-analyser.git
cd academic-performance-analyser
```

### ✅ Step 2: Install required packages

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install streamlit pandas openpyxl
```

### ✅ Step 3: Run the Streamlit app

```bash
streamlit run app.py
```

Then open the local URL (usually `http://localhost:8501`) in your browser.

---

## 📂 Files in the Repository

| File                          | Purpose                                |
|-------------------------------|----------------------------------------|
| `app.py`                      | Main Streamlit dashboard code          |
| `Anonymized_CPI_SPI_Data.xlsx`| Anonymized CPI/SPI dataset             |
| `README.md`                   | Project documentation                  |
| `requirements.txt`            | Python dependencies                    |

---

## 🔐 Disclaimer on Data Privacy

This project uses **anonymized academic data** for demonstration purposes only.

- All **student names and roll numbers** are synthetic and anonymized (e.g., “Student 1”, “ID0001”)
- The CPI/SPI values are retained to show meaningful trends, but **no personally identifiable information (PII)** is included
- This dataset is intended strictly for **educational and non-commercial** use

---

## 👨‍💻 Author

**Raghvendra Singh**  
🎓 3rd Year Undergraduate, IIT Kanpur  
🔗 [LinkedIn](https://www.linkedin.com/in/raghvendra-singh-59102a286/)  
💻 [GitHub](https://github.com/raghvendra253)

---

## 🌟 Star this repo if you find it useful!
