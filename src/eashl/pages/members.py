import streamlit as st
from eashl.util.scraper import load_member_data
from eashl.util.helpers import generate_overview_df, generate_goals_df
from eashl.schemas.member import MembersData

st.set_page_config(page_title="EASHL Stats Hub | Simulator", layout="wide")
st.title("Club Member Stats")
st.markdown("Displays player level breakdown for the club")

with st.sidebar:
    club_id: str = st.text_input("Club", value="0")


def render_data() -> None:
    data: MembersData = load_member_data(club_id)

    st.title("Player Stats Viewer")

    overview_df = generate_overview_df(data)

    st.header("Player Overview")
    st.table(overview_df)

    goals_df = generate_goals_df(data)

    st.header("Scoring Breakdown")
    st.table(goals_df)


render_data()
