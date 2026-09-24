import streamlit as st
st.title("My Streamlit App")
st.text("Welcome to my Streamlit application!")
st.image("arun.png", caption="My Image",width=400)


st.text_input("Enter your name:", key="username")
st.text_input("Enter your password:", type="password", key="password")
if st.button("login"):
    if st.session_state.username == "arun" and st.session_state.password == "password":
        st.success("Login successful!") 
    else:
        st.error("Invalid username or password.")
        
           