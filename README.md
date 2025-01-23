# Apple_Quality_Prediction
"This project predicts the quality of apples (good or bad) based on features like size, weight, sweetness, crunchiness, juiciness, ripeness, and acidity using a trained machine learning model, and provides an interactive web interface via Streamlit for users to input data and view predictions."

<img src="https://github.com/rpjinu/Apple_Quality_Prediction/blob/main/project_image.png">

# 🍎 Apple Quality Prediction Project

This project predicts the quality of apples (good or bad) based on features like size, weight, sweetness, crunchiness, juiciness, ripeness, and acidity using a trained machine learning model. It also provides an interactive web interface via **Streamlit** for users to input data and view predictions.

---

## 📋 Table of Contents
1. [Project Overview](#-project-overview)
2. [Features](#-features)
3. [Technologies Used](#-technologies-used)
4. [Dataset](#-dataset)
5. [Steps to Build the Project](#-steps-to-build-the-project)
6. [How to Run the Project](#-how-to-run-the-project)
7. [Deployment](#-deployment)
8. [Contributing](#-contributing)
9. [License](#-license)

---

## 🚀 Project Overview

The goal of this project is to build a machine learning model that can predict the quality of apples based on various features. The model is trained on a dataset containing apple features and their corresponding quality labels (`good` or `bad`). Once trained, the model is deployed as an interactive web application using **Streamlit**, where users can input feature values and get real-time predictions.

---

## 🌟 Features

- **Machine Learning Model**: A Random Forest classifier is used to predict apple quality.
- **Interactive Web Interface**: Built using **Streamlit**, the app allows users to input apple features and view predictions.
- **Scalable**: The model can be easily retrained with new data for better accuracy.
- **User-Friendly**: Simple and intuitive interface for users to interact with.

---

## 🛠 Technologies Used

- **Python**: Primary programming language.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For building and training the machine learning model.
- **Streamlit**: For creating the interactive web application.
- **Joblib**: For saving and loading the trained model.
- **Git/GitHub**: For version control and project hosting.

---

## 📊 Dataset

The dataset used in this project contains the following features:

| Feature      | Description                          |
|--------------|--------------------------------------|
| Size         | Size of the apple (numeric value).   |
| Weight       | Weight of the apple (numeric value). |
| Sweetness    | Sweetness level of the apple.        |
| Crunchiness  | Crunchiness level of the apple.      |
| Juiciness    | Juiciness level of the apple.        |
| Ripeness     | Ripeness level of the apple.         |
| Acidity      | Acidity level of the apple.          |
| Quality      | Target variable: `good` or `bad`.    |

---

## 🛠 Steps to Build the Project

### 1. **Data Preparation**
   - Load the dataset using Pandas.
   - Perform exploratory data analysis (EDA) to understand the data distribution and relationships.
   - Map the target variable (`Quality`) to numerical values: `good` → `1`, `bad` → `0`.

### 2. **Model Training**
   - Split the dataset into training and testing sets.
   - Train a Random Forest classifier using Scikit-learn.
   - Evaluate the model using metrics like accuracy, confusion matrix, and classification report.

### 3. **Save the Model**
   - Save the trained model and preprocessing objects (e.g., scaler, mapping dictionary) using Joblib.

### 4. **Build the Streamlit App**
   - Create an interactive web interface using Streamlit.
   - Allow users to input apple features and display the predicted quality.

### 5. **Test the App**
   - Run the Streamlit app locally and test it with various inputs.

### 6. **Deploy the App**
   - Deploy the app using platforms like **Streamlit Sharing**, **Heroku**, or **AWS**.

---

## 🖥 How to Run the Project

### Prerequisites
- Python 3.8 or higher.
- Required Python libraries: `pandas`, `scikit-learn`, `streamlit`, `joblib`.

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/apple-quality-prediction.git
   cd apple-quality-prediction
