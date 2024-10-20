from typing import List
from dataclasses import dataclass
from ortools.sat.python import cp_model


@dataclass
class Journey:
    "This class is the points a player had in a concrete game (Journey)"
    numberJourney: int
    pointsJourney: int


@dataclass
class BasketPlayer:
    """Class for ABC Supermanager Player."""
    age: int
    competitionAverage: float
    down15: float
    fisicStatus: str
    fullName: str
    height: str
    initialPrice: float
    injuredDays: int
    isActive: bool
    isBlock: bool
    isExitLeague: bool
    isExtraCommunity: bool
    isNational: bool
    keep: float
    license: str
    nameTeam: str
    nick: str
    playerStats: List
    position: int
    price: float
    shortName: str
    up15: float


# read current team and market

model = cp_model.CpModel()


solver = cp_model.CpSolver()