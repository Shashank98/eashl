from eashl.schemas.member import MembersData
import pandas


def generate_overview_df(data: MembersData) -> pandas.DataFrame:
    table_data = [
        {
            "Name": member.name,
            "Favorite Position": member.favoritePosition,
            "Games Played": member.gamesplayed,
            "Record": member.record,
        }
        for member in data.members
    ]

    return pandas.DataFrame(table_data)
