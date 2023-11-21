import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB



diabetes_model_dtr = pickle.load(open('decisiontree_model.pkl', 'rb'))
diabetes_model_knn = pickle.load(open('knn_model.pkl', 'rb'))
diabetes_model_nvb = pickle.load(open('nvb_model.pkl', 'rb'))

st.title("Prediksi diabetes menggunakan 3 model machine learning")

age = st.text_input('Input Umur')

# Convert gender to 0 or 1
gender = st.selectbox('Input Gender', ['Male', 'Female'])
gender = 0 if gender == 'Female' else 1

impluse = st.text_input('Input impluse')
pressurehight = st.text_input('Input pressurehight')
pressurelow = st.text_input('Input pressurelow')
glucose = st.text_input('Input glucose')
kcm = st.text_input('Input kcm')
troponin = st.text_input('Input troponin')

diagnosis_dtr = ''
diagnosis_knn = ''
diagnosis_nvb = ''

if st.button('Test Prediksi Diabetes'):
    input_data = [[age, gender, impluse, pressurehight, pressurelow, glucose, kcm, troponin]]
    
    diagnosis_dtr = diabetes_model_dtr.predict(input_data)
    diagnosis_knn = diabetes_model_knn.predict(input_data)
    diagnosis_nvb = diabetes_model_nvb.predict(input_data)

    if diagnosis_dtr[0] == 1:
        diagnosis_dtr = "Pasien terkena diabetes (dtr)"
    else:
        diagnosis_dtr = "Pasien tidak terkena diabetes(dtr)"

    if diagnosis_knn[0] == 1:
        diagnosis_knn = "Pasien terkena diabetes (knn)"
    else:
        diagnosis_knn = "Pasien tidak terkena diabetes(knn)"

    if diagnosis_nvb[0] == 1:
        diagnosis_nvb = "Pasien terkena diabetes (nvb)"
    else:
        diagnosis_nvb = "Pasien tidak terkena diabetes(nvb)"
