from eashl.schemas.member import MembersData
import pandas


def generate_overview_df(data: MembersData) -> pandas.DataFrame:
    table_data = [
        {
            "Name": member.name,
            "Favorite Position": member.favoritePosition,
            "Games Played": member.gamesplayed,
            "Record": member.record,
            "Win %": member.winpct,
            "DNF": member.DNF,
            "+/-": member.plusmin,
        }
        for member in data.members
    ]

    return pandas.DataFrame(table_data)


def generate_goals_df(data: MembersData) -> pandas.DataFrame:
    table_data = [
        {
            "Name": member.name,
            "Goals": member.goals,
            "Assists": member.assists,
            "Points": member.points,
            "Game Winning Goals": member.gwg,
            "Shots/Game": member.shotspg,
            "Shots on Net %": member.shotonnetpct,
            "Breakaway Goals": member.brkgoals,
            "Breakaway %": member.breakawaypct,
            "Hattricks": member.hattricks,
        }
        for member in data.members
    ]

    return pandas.DataFrame(table_data)
