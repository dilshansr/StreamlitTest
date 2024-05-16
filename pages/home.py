import streamlit as st

def show(name):
    st.title("Home Page")
    if name:
        st.write(f"Welcome to the Home Page, {name}!")
    else:
        st.write("Welcome to the Home Page.")
    name_input = st.text_input("Enter your name:", value=name)
    if st.button("Go to Page 1"):
        st.experimental_set_query_params(page='page1', name=name_input)
    if st.button("Go to Page 2"):
        st.experimental_set_query_params(page='page2', name=name_input)

