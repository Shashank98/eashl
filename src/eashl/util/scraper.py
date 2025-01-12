import requests
import json
from typing import Any
from pydantic import ValidationError
from eashl.schemas.member import MembersData
from eashl.constants import BASE_URL, MEMBERS_URL

from logging import getLogger

logger = getLogger(__name__)


def fetch_json(url: str) -> Any:
    """
    Makes a GET request to the given URL and loads the result into a JSON object.

    Args:
        url (str): The URL to make the GET request to.

    Returns:
        dict: The response JSON as a Python dictionary if successful.
        None: If the request fails or the response is not valid JSON.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Referer": "www.ea.com",
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        return None


def load_member_data(club_id: int) -> MembersData:
    print("Loading member data")
    # Example usage
    url = f"{BASE_URL}{MEMBERS_URL}{club_id}"
    data = fetch_json(url)

    if data:
        try:
            # Parse the data into the Pydantic model
            members_data = MembersData.parse_obj(data)
        except ValidationError as e:
            print("Failed to validate the data with the Pydantic model:")
            print(e.json())

    return members_data
