#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu


data = pd.read_csv("Scholarshipsnew.csv")



# st.sidebar.header("Navigation")
# navigation = st.sidebar.radio("Navigation",["Home","About Us","List of Government Funded Scholarships","List of Private Funded Scholarships","Specially for Women Scholarships"], label_visibility="hidden")

with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home","About Us","Government Funded Scholarships","Private Funded Scholarships","Scholarship for Women","International Scholarships"],
        icons=["house","compass","envelope","geo","gender-female",""],
        default_index=0,
        menu_icon="cast", 
        orientation="horizontal"
    )
    


if selected == "Home":
    st.title("Scholarship Finder")
    # st.dataframe(data)
    name = st.text_input("Enter your Name",placeholder="Name")
    if len(name) >= 1:
        minority = st.radio("Are you in Minorities(SC/ST) category?" ,["Yes","No"],index=1)
        disability = st.radio("Do you have any disablity?",["Yes","No"],index=1)
        sports_person = st.radio("Do you play professional sports?",["Yes","No"],index=1)
        armed_forces = st.radio("Are any of ur realtive in Armed Forces??",["Yes","No"],index=1)
        anual_income = st.number_input("Enter your family's annual income",max_value=1100000)
        if anual_income >= 1100000:
            st.info("Annual Income should be less than 10 Lakh Rupees")
        marks = st.slider("Enter your marks in last final examination",min_value=0,max_value=100,value=30,step=1)
        gender = st.selectbox("Enter your gender:",["Male","Female"])
        nationality = st.radio("Do you want to include International Scholarships",["Yes","No"])
       
        if gender == "Female":
            if nationality == "Yes":
                mask = data.loc[(data["Minorities"] == minority) & (data["Annual Income"] >= anual_income ) & (data["Disablities"] == disability) & (data["Armed Forces"] == armed_forces) & (data["Sports Person"] == sports_person) & (data["Grades in Prev Exam"] <= marks)]
            else:
                mask = data.loc[(data["Minorities"] == minority) & (data["Annual Income"] >= anual_income ) & (data["Disablities"] == disability) & (data["Armed Forces"] == armed_forces) & (data["Sports Person"] == sports_person) & (data["Grades in Prev Exam"] <= marks) & (data["Country"] == "India") ]
        else:
            if nationality == "Yes":
                # st.write(nationality)
                mask = data.loc[(data["Minorities"] == minority) & (data["Annual Income"] >= anual_income ) & (data["Disablities"] == disability) & (data["Armed Forces"] == armed_forces) & (data["Sports Person"] == sports_person) & (data["Grades in Prev Exam"] <= marks) & (data["Gender"] == "No")]
            else:
                mask = data.loc[(data["Minorities"] == minority) & (data["Annual Income"] >= anual_income ) & (data["Disablities"] == disability) & (data["Armed Forces"] == armed_forces) & (data["Sports Person"] == sports_person) & (data["Grades in Prev Exam"] <= marks) & (data["Gender"] == "No") & (data["Country"] == "India")]
        mask_new = mask[["Scholarship Name" , "Amount Provided","Link" ,"Funded By"]]
        rows = mask_new.shape[0]
        cols = mask_new.shape[1]
        a = []
        for i in range(rows):
            a.append(f"{ mask_new.iloc[i,0] } : {mask_new.iloc[i,1]} Rs \n {mask_new.iloc[i,2]} \n\n")
            a.append("-------------------------------------------")
        if st.button("Submit"):   
            for i in range(len(a)):
                st.write(a[i])
    else:
        st.info("This can't be empty!")

if selected == "Government Funded Scholarships":
    st.header("Government Funded Scholarships")
    new = data["Funded By"] == "Government"
    govt_funded = data[new]
    govt_funded = govt_funded[["Scholarship Name" , "Amount Provided","Link"]]
    st.table(govt_funded)

if selected == "Private Funded Scholarships":
    st.header("Private Funded Scholarships")
    new_2 = data["Funded By"] == "Private"
    prvt_funded = data[new_2]
    prvt_funded = prvt_funded[["Scholarship Name" , "Amount Provided","Link"]]
    st.table(prvt_funded)

if selected == "Scholarship for Women":
    st.header("Specifically For Women")
    new_3 = data["Gender"] == "Yes"
    women_funded = data[new_3]
    women_funded = women_funded[["Scholarship Name" , "Amount Provided","Link"]]
    st.table(women_funded)

if selected == "International Scholarships":
    st.header("International Scholarships")
    new_4 = data["Country"] != "India"
    international_funded = data[new_4]
    international_funded = international_funded[["Scholarship Name" , "Amount Provided","Link"]]
    st.table(international_funded)






