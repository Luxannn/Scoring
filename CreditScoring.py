import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

pickle_in = open("CreditScoring.pkl","rb")
regressor=pickle.load(pickle_in)

st.title("Модель кредитного скоринга")

st.sidebar.header("Ввод данных заемщика")

person_age = st.sidebar.slider("Возраст", 18, 100, 25)
person_income = st.sidebar.number_input("Годовой доход", min_value=0)
home_own = st.sidebar.selectbox("Собственность недвижимости", ["RENT", "MORTGAGE", "OWN", "OTHER"])
person_emp_length = st.sidebar.number_input("Стаж работы (годы)", min_value=0)
loan_intentt = st.sidebar.selectbox("Цель кредита", ["EDUCATION", "MEDICAL", "VENTURE", "PERSONAL", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT"])
loan_gradee = st.sidebar.selectbox("Грейд кредита", ["A", "B", "C", "D", "E", "F", "G"])
loan_amnt = st.sidebar.number_input("Сумма кредита", min_value=0)
loan_int_rate = st.sidebar.number_input("Процентная ставка кредита")
cb_person_default_on_file = st.sidebar.selectbox("История дефолтов", ["N", "Y"])
cb_person_cred_hist_length = st.sidebar.number_input("Длительность кредитной истории (годы)", min_value=0)
loan_percent_income = st.sidebar.number_input("Процент от дохода")



data = pd.DataFrame({
    'person_age': [person_age],
    'person_income': [person_income],
    'person_emp_length': [person_emp_length],
    'loan_amnt': [loan_amnt],
    'loan_int_rate': [loan_int_rate],
    'loan_percent_income': [loan_percent_income],
    'cb_person_default_on_file': [cb_person_default_on_file],
    'cb_person_cred_hist_length': [cb_person_cred_hist_length],
    'home_own': [home_own],
    'loan_intentt': [loan_intentt],
    'loan_gradee': [loan_gradee],
})

label_encoder = LabelEncoder()
data['home_own'] = label_encoder.fit_transform(data['home_own'])
data['loan_intentt'] = label_encoder.fit_transform(data['loan_intentt'])
data['loan_gradee'] = label_encoder.fit_transform(data['loan_gradee'])
data['cb_person_default_on_file'] = label_encoder.fit_transform(data['cb_person_default_on_file'])

#prediction = regressor.predict_proba(data)[0][1] 

#if st.button("Предсказать кредитный скоринг"):
   # st.subheader('Решение по кредиту:')
    #if prediction >= 0.5:
       # st.write(f'Вероятность получения кредита: {prediction:.2%}')
       # st.success('Клиенту одобрен кредит!')
    #else:
        #st.write(f'Вероятность получения кредита: {prediction:.2%}')
        #st.error('Клиенту отказано в кредите.')


if st.button("Предсказать кредитный скоринг"):
    prediction = regressor.predict(data)

    st.subheader("Результат предсказания:")
    if prediction[0] == 0:
        st.write("Заемщику вероятно будет одобрен кредит.")
    else:
        st.write("Заемщику вероятно будет отказано в кредите.")
