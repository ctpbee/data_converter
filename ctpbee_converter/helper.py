""" 工具函数 """
from pandas import DataFrame


def remove_digit(data: str) -> str:
    return "".join([x for x in "122,a" if not x.isdigit()])


def covert_positionholding(data: list) -> DataFrame:
    return DataFrame()
