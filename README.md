# 💳 Credit Card Fraud Detection using Machine Learning

A Machine Learning web application that detects whether a credit card transaction is **Fraudulent** or **Legitimate** using a **Random Forest Classifier**. The project is deployed with **Streamlit** and provides real-time predictions through an interactive user interface.

---

## 📌 Overview

Credit card fraud is one of the most significant challenges faced by financial institutions. This project applies Machine Learning techniques to identify fraudulent transactions based on historical transaction data.

The application allows users to enter transaction details and instantly predicts whether the transaction is legitimate or fraudulent.

---

## ✨ Features

- 🔍 Real-time fraud detection
- 🌐 Interactive Streamlit web application
- 🤖 Random Forest Classifier
- 📊 Feature scaling using StandardScaler
- ⚡ Fast prediction with trained model
- 💾 Pre-trained model using Pickle
- 📱 Clean and user-friendly interface

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

## 📂 Project Structure

```
Credit-Card-Fraud-Detection/
│
├── app.py
├── credit_card_fraud_detection.py
├── model.pkl
├── scaler.pkl
├── creditcard.csv
├── requirements.txt
├── README.md
└── assets/
    ├── banner.png
    ├── app_home.png
    └── prediction.png
```

---

## 📊 Dataset

The project uses the **Credit Card Fraud Detection Dataset**, which contains anonymized transactions made by European cardholders.

### Input Features

- Time
- V1 – V28 (PCA-transformed features)
- Amount

### Target Variable

| Value | Meaning |
|-------|---------|
| 0 | Legitimate Transaction |
| 1 | Fraudulent Transaction |

---

## 🤖 Machine Learning Workflow

1. Import Dataset
2. Data Cleaning
3. Remove Missing Values
4. Remove Duplicate Records
5. Train-Test Split
6. Feature Scaling using StandardScaler
7. Train Random Forest Classifier
8. Evaluate Model Performance
9. Save Model using Pickle
10. Deploy with Streamlit

---

## 📈 Model Information

**Algorithm Used**

- Random Forest Classifier

**Preprocessing**

- StandardScaler

**Saved Files**

- `model.pkl`
- `scaler.pkl`

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/sanyamjain-2006/Credit-Card-Fraud-Detection.git
```

### Navigate to Project

```bash
cd Credit-Card-Fraud-Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

---

## 💻 Application Preview

### Home Page

> *(Add a screenshot of your Streamlit application's home page here.)*

### Prediction Result

> *(Add a screenshot showing the prediction result here.)*

---

## 📌 Future Enhancements

- Batch prediction using CSV upload
- Fraud probability visualization
- Feature importance chart
- Dark mode UI
- Prediction history
- Interactive dashboard
- Cloud deployment improvements

---

## 📷 Screenshots

| Home | Prediction |
|------|------------|
| Add Screenshot | Add Screenshot |

---

## 📜 Requirements

```
streamlit
pandas
numpy
scikit-learn==1.6.1
```

---

## 👨‍💻 Author

**Sanyam Jain**

**B.Tech - Artificial Intelligence & Machine Learning**

- Python Developer
- Machine Learning Enthusiast
- Data Science Learner

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates further development.
