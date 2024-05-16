import streamlit as st
from pages import home, page1, page2

def get_query_params():
    query_params = st.experimental_get_query_params()
    return query_params

def main():
    query_params = get_query_params()
    page = query_params.get('page', ['home'])[0]
    name = query_params.get('name', [''])[0]

    if page == 'home':
        home.show(name)
    elif page == 'page1':
        page1.show(name)
    elif page == 'page2':
        page2.show(name)

if __name__ == "__main__":
    st.sidebar.markdown("[Home](?page=home)")
    st.sidebar.markdown("[Page 1](?page=page1)")
    st.sidebar.markdown("[Page 2](?page=page2)")
    main()
