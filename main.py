import pickle
import sklearn
import numpy as np
import pandas as pd
import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = 0

def nextpage():
    if username == "admin" and password == "123":
        st.session_state.page += 1
    else:
        st.error("Incorrect username or password")

def restart(): st.session_state.page = 0

if st.session_state.page == 0:
    # Replace the placeholder with some text:
    st.header(':blue[Login]')
    username = st.text_input("**Username:**")
    password = st.text_input("**Password:**", type="password")
    st.button("**Submit**", on_click=nextpage)


elif st.session_state.page == 1:

    with open('fraud_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Streamlit page
    st.header(':blue[Transaction Fraud Prediction]')

    options1 = ["0:Entertainment", "1:Food_dining", '2:Gas_transport',
                '3:Grocery_net', '4:Grocery_pos', '5:health_fitness', '6:Home', '7:Kids_pet', '8:Misc_net', '9:Misc_pos',
                '10:Personal_care', '11:Shopping_net', '12:Shopping_pos', '13:Travel']
    cat = st.selectbox("**:green[Category of Transaction]**", options1)
    cat = float(cat.split(':')[0])
    options2 = ["0:Male", "1:Female"]
    gen = st.selectbox("**:green[Gender]**", options2)
    gen = float(gen.split(':')[0])
    num = st.number_input('**:green[Amount of Transaction in K]**')
    sub = st.button('**Check Transaction**')

    new_data = np.array([[cat, num, gen]])


    # make predictions using the model
    def predict(new_data):
        predictions = model.predict(new_data)
        return predictions


    # prediction function
    if sub:
        predictions = predict(new_data)
        if predictions[0] == 0:
            st.success('This Transaction is Safe.', icon="✅")
        else:
            st.error('This Trasaction may be Fraudlent.', icon="⚠️")
