import streamlit as st
import pickle

    

diabetes_model_dtr = pickle.load(open('decisiontree_model.pkl', 'rb'))
diabetes_model_knn = pickle.load(open('knn_model.pkl', 'rb'))
diabetes_model_nvb = pickle.load(open('nvb_model.pkl', 'rb'))

st.title("Prediksi diabetes menggunakan 3 model machine learning")

age = st.number_input('Input Umur', value=0, step=1)

# Convert gender to 0 or 1
gender = st.selectbox('Input Gender', ['Male', 'Female'])
gender = 0 if gender == 'Female' else 1

impluse = st.number_input('Input impluse', value=0, step=1)
pressurehight = st.number_input('Input pressurehight', value=0, step=1)
pressurelow = st.number_input('Input pressurelow', value=0, step=1)
glucose = st.number_input('Input glucose', value=0, step=1)
kcm = st.number_input('Input kcm', value=0, step=1)
troponin = st.number_input('Input troponin', value=0, step=1)

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
