import streamlit as st
from streamlit.navigation.page import StreamlitPage

page: StreamlitPage = st.navigation(
    [
        st.Page("pages/home.py", title="Home"),
        st.Page("pages/members.py", title="Member Stats"),
    ]
)
page.run()
