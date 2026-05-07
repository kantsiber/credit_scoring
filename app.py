import streamlit as st
import requests

st.markdown("""
    <style>
        .stApp {
            background-color: #2b2b2b;
        }
    </style>
""", unsafe_allow_html=True)

st.title('Кредитный скоринг')
st.write('Проверь одобрят ли тебе кредит')

with st.form('Подать заявку'):
    age = st.number_input('Ваш возраст', min_value=18)
    income = st.number_input('Ваш доход в тысячах', min_value=0)
    education = st.checkbox('Наличие высшего образования')
    work = st.checkbox('Наличие стабильной работы')
    car = st.checkbox('Наличие машины')
    submit = st.form_submit_button('Подать заявку')

if submit:
    data = {
        'age': age,
        'income': income,
        'education': education,
        'work': work,
        'car': car
    }
    response = requests.post('http://127.0.0.1:8000/score', json=data)
    if response.json()['approved']:
        st.success('У вас есть шансы на одобрение кредита!')
    else:
        st.error('Ваши шансы малы, стоит немного наладить быт!')