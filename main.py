from helper import *
import streamlit as st
import os

st.write("""
# Titanic Survival Predictor App
See if you or your made up person would survive the Titanic!
""")
st.write('---')

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    sex = st.sidebar.selectbox("Sex",("Male", "Female"))
    title = st.sidebar.selectbox("Title",("Miss", "Mr", "Mrs", "Officer", "Royalty"))
    age = st.sidebar.selectbox("Age",("Child", "Teen", "Student", "Young Adult", "Adult", "Senior"))
    fsize = st.sidebar.slider("Family Size", 1, 15, 1)
    pclass = st.sidebar.slider("Passenger Class", 1, 3, 1)
    fare = st.sidebar.selectbox("Fare Paid",("Free", "Cheap", "Regular", "Expensive"))
    embarked = st.sidebar.selectbox("Port Embarked", ("Cherbourg", "Queenstown", "Southampton"))

    if sex == "Male":
        sex = 1
    else:
        sex = 0

    if title == "Miss":
        title = 1
    elif title == "Mr":
        title = 2
    elif title == "Mrs":
        title = 3
    elif title == "Officer":
        title = 4
    else:
        title = 5

    if age == "Child":
        age = 1
    elif age == "Teen":
        age = 2
    elif age == "Student":
        age = 3
    elif age == "Young Adult":
        age = 4
    elif age == "Adult":
        age = 5
    else:
        age = 6
    
    if fare == "Free":
        fare = 1
    elif fare == "Cheap":
        fare = 2
    elif fare == "Regular":
        fare = 3
    else:
        fare = 4

    if embarked == "Queenstown":
        embarked = 1
    elif embarked == "Southampton":
        embarked = 2
    else:
        embarked = 3

    return title, pclass, fsize, sex, embarked, age, fare

title, pclass, fsize, sex, embarked, age, fare = user_input_features()

# Get prediction
surv = predict_survival(title, pclass, fsize, sex, embarked, age, fare)

if surv == 1:
    st.write("""
    ## Based on your input, it is predicted that you WILL survive!
    """)
else:
    st.write("""
    ## Based on your input, it is predicted that you WILL NOT survive!
    """)