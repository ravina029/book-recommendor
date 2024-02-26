import pickle
import streamlit as st 
import numpy as np

st.header("Book Recommender System using ML algorithm")
model=pickle.load(open("artifacts/model.pkl"),'rb')
bookname=pickle.load(open("artifacts/book_name.pkl"),'rb')
book_pivot=pickle.load(open("artifacts/book_pivot.pkl"),'rb')
rating=pickle.load(open("artifacts/final_rating.pkl"),'rb')

chosed_books=st.selectbox(
    "Select or Enter the name of the book",


)
