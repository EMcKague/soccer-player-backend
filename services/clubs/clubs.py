from typing import Any

from helpers.array import get_random_index_from_list


class Clubs:
    club_list = [
        "Arsental",
        "Atletico Madrid",
        "FC Bayern",
        "Bayer 04",
        "Liverpool",
        "Real Madrid",
        "Manchester City",
        "Chelsea",
        "Juventus",
        "Manchester Utd",
    ]

    @classmethod
    def get_random_club(cls) -> str:
        return get_random_index_from_list(cls.club_list)
