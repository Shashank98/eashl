import streamlit as st

from logging import getLogger

logger = getLogger(__name__)

st.set_page_config(page_title="EASHL Stats Hub | Home", layout="wide")
st.title("EASHL Stats Hub")

row1 = st.columns(3)
row2 = st.columns(3)

col = row1[0]
tile = col.container()
tile.page_link("pages/members.py", icon=":material/list:")
