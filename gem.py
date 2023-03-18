import streamlit as st

def say_hello():
    st.write("Hello gem")

if st.button("Say hello"):
    say_hello()