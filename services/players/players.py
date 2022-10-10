from random import randint
from typing import List
from pydantic import BaseModel
from helpers.array import get_random_index_from_list
from services.clubs.clubs import Clubs

from services.countries.countries import Countries


class Player(BaseModel):
    id: int
    name: str
    nationality: str
    club: str
    national_position: str
    preffered_foot: str
    age: int
    goals: int
    assists: int
    height: int

    @classmethod
    def index(cls) -> List["Player"]:
        max = 11
        # print([cls._get_random_player(number) for number in range(max)])
        return [
            Player(
                id=0,
                name="Jackmerius Tacktheritrix",
                nationality="Morocco",
                club="Real Madrid",
                national_position="ST",
                preffered_foot="Right",
                age=32,
                goals=9,
                assists=48,
                height=183,
            ),
            Player(
                id=1,
                name="Swirvithan L'Goodling-Splatt",
                nationality="Mauritius",
                club="Atletico Madrid",
                national_position="ST",
                preffered_foot="Right",
                age=37,
                goals=75,
                assists=88,
                height=164,
            ),
            Player(
                id=2,
                name="Squeeeeeeeeeeps",
                nationality="Congo",
                club="Manchester Utd",
                national_position="LM",
                preffered_foot="Left",
                age=27,
                goals=19,
                assists=14,
                height=169,
            ),
            Player(
                id=3,
                name="Eqqsnuizitine Buble-Schwinslow",
                nationality="Gabon",
                club="Atletico Madrid",
                national_position="RW",
                preffered_foot="Right",
                age=28,
                goals=58,
                assists=28,
                height=169,
            ),
            Player(
                id=4,
                name="Harvard University",
                nationality="Kenya",
                club="Arsental",
                national_position="LM",
                preffered_foot="Right",
                age=29,
                goals=22,
                assists=64,
                height=179,
            ),
            Player(
                id=5,
                name="Elipses Corter",
                nationality="Tuvalu",
                club="Juventus",
                national_position="GK",
                preffered_foot="Right",
                age=27,
                goals=0,
                assists=0,
                height=157,
            ),
            Player(
                id=6,
                name="Xmus Jaxon Flaxon-Waxon",
                nationality="Malawi",
                club="Chelsea",
                national_position="GK",
                preffered_foot="Left",
                age=37,
                goals=0,
                assists=0,
                height=170,
            ),
            Player(
                id=7,
                name="Shakiraquan T.G.I.F. Carter",
                nationality="Sierra Leone",
                club="Real Madrid",
                national_position="GK",
                preffered_foot="Right",
                age=31,
                goals=0,
                assists=0,
                height=172,
            ),
            Player(
                id=8,
                name="T'varisuness King",
                nationality="Wallis and Futuna",
                club="Manchester Utd",
                national_position="LW",
                preffered_foot="Left",
                age=24,
                goals=40,
                assists=77,
                height=156,
            ),
            Player(
                id=9,
                name="Equine Ducklings",
                nationality="Saint Kitts and Nevis",
                club="Real Madrid",
                national_position="Sub",
                preffered_foot="Right",
                age=23,
                goals=26,
                assists=90,
                height=164,
            ),
            Player(
                id=10,
                name="Benedict Cumberbatch",
                nationality="Nauru",
                club="Manchester Utd",
                national_position="RW",
                preffered_foot="Left",
                age=39,
                goals=37,
                assists=92,
                height=178,
            ),
        ]

    @classmethod
    def _get_random_player(cls, id: int):
        player = Player(
            id=id,
            name=cls._get_random_name(),
            nationality=Countries.get_random_country(),
            club=Clubs.get_random_club(),
            national_position=cls._get_random_position(),
            preffered_foot=cls._get_random_preffered_foot(),
            age=cls._get_random_age(),
            goals=cls._get_random_goals(),
            assists=cls._get_random_assists(),
            height=cls._get_random_height(),
        )
        if player.national_position == "GK":
            player.goals = 0
            player.assists = 0
        return player

    @classmethod
    def _get_random_name(cls):
        names = [
            "D'Marcus Williums" "T.J. Juckson",
            "T'varisuness King",
            "Tyroil Smoochie-Wallace",
            "D'Squarius Green, Jr.",
            "Ibrahim Moizoos",
            "Jackmerius Tacktheritrix",
            "D'Isiah T. Billings-Clyde",
            "D'Jasper Probincrux III",
            "Leoz Maxwell Jilliumz",
            "Javaris Jamar Javarison-Lamar",
            "Davoin Shower-Handel",
            "Hingle McCringleberry",
            "L'Carpetron Dookmarriot",
            "J'Dinkalage Morgoone",
            "Xmus Jaxon Flaxon-Waxon",
            "Saggitariutt Jefferspin",
            "D'Glester Hardunkichud",
            "Swirvithan L'Goodling-Splatt",
            "Quatro Quatro",
            "Ozamataz Buckshank",
            "Beezer Twelve Washingbeard",
            "Shakiraquan T.G.I.F. Carter",
            "X-Wing @Aliciousness",
            "Sequester Grundelplith M.D.",
            "Scoish Velociraptor Maloish",
            "T.J. A.J. R.J. Backslashinfourth V",
            "Eeeee Eeeeeeeee",
            "Donkey Teeth",
            "Torque (Construction Noise) Lewith",
            "The Player Formerly Known as Mousecop",
            "Dan Smith",
            "Coznesster Smiff",
            "Elipses Corter",
            "Nyquillus Dillwad",
            "Bismo Funyuns",
            "Decatholac Mango",
            "Mergatroid Skittle",
            "Quiznatodd Bidness",
            "D'Pez Poopsie",
            "Quackadilly Blip",
            "Goolius Boozler",
            "Bisquiteen Trisket",
            "Fartrell Cluggins",
            "Blyrone Blashinton",
            "Cartoons Plural",
            "Jammie Jammie-Jammie",
            "Fudge",
            "Equine Ducklings",
            "Dahistorius Lamystorius",
            "Ewokoniad Sigourneth JuniorStein",
            "Eqqsnuizitine Buble-Schwinslow",
            "Huka'lakanaka Hakanakaheekalucka'hukahakafaka",
            "King Prince Chambermaid",
            "Ladennifer Jadaniston",
            "Ladadadaladadadadada Dala-Dadaladaladalada",
            "Harvard University",
            "Morse Code",
            "Wingdings",
            "Firstname Lastname",
            "Squeeeeeeeeeeps",
            "Benedict Cumberbatch",
            "A.A. Ron Balakay",
        ]
        return get_random_index_from_list(some_list=names)

    @classmethod
    def _get_random_height(cls):
        return randint(155, 185)

    @classmethod
    def _get_random_preffered_foot(cls):
        return get_random_index_from_list(["Right", "Left"])

    @classmethod
    def _get_random_position(cls):
        positions = [
            "LW",
            "CAM",
            "RW",
            "CDM",
            "Sub",
            "LCB",
            "LS",
            "LM",
            "GK",
            "ST",
            "RS",
        ]
        return get_random_index_from_list(positions)

    @classmethod
    def _get_random_age(cls):
        return randint(18, 40)

    @classmethod
    def _get_random_goals(cls):
        return randint(0, 100)

    @classmethod
    def _get_random_assists(cls):
        return randint(0, 100)
