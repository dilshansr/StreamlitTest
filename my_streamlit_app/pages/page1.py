import streamlit as st

def show(name):
    st.title("Page 1")
    name_input = st.text_input("Your name:", value=name)
    st.write(f"Hello, {name}, you are on Page 1.")
    if st.button("Update Name"):
        st.experimental_set_query_params(page='page1', name=name_input)
    st.markdown("[Go Home](?page=home&name={})".format(name_input))
