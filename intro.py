import streamlit as st

st.title("My Web ApP")

st.header("This is a header")

st.write("Learning Streamlit for the first time")

agree = st.checkbox("I agree with Vickey")

if agree:
    st.write("You are awesome")

genre = st.radio("What is your favoriate movie genre ? ", ["Comedy", "Drama", "Documentary"])

if genre == "Comedy":
    st.write("You selected Comedy")
elif genre == "Drama":
    st.write("You selected Drama")
else:
    st.write("You selected Documentary")