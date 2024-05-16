import streamlit as st

def show(name):
    st.title("Page 2")
    name_input = st.text_input("Your name:", value=name)
    st.write(f"Hello, {name}, you are on Page 2.")
    if st.button("Update Name"):
        st.experimental_set_query_params(page='page2', name=name_input)
    st.markdown("[Go Home](?page=home&name={})".format(name_input))
