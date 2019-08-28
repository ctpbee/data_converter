""" 工具函数 """
from typing import List, Dict, Any

from pandas import DataFrame


def remove_digit(data: str) -> str:
    return "".join([x for x in data if not x.isdigit()])


def convert_ld_to_dict(data: List[Dict,]):
    """ 将[ {}, {}, {}] -->转换为 {key:[]}"""
    resust = {}
    for x in data:
        for i, v in x.items():
            if i in resust:
                resust[i] = resust[i] + [v]
            else:
                resust.setdefault(i, [v])
    return resust


def convert_lo_to_dict(data: List[Any,]):
    resust = {}
    for x in data:
        for i, v in x._to_dict().items():
            if i in resust:
                resust[i] = resust[i] + [v]
            else:
                resust.setdefault(i, [v])
    return resust


def convert_d_to_df(data: Dict):
    return DataFrame(data=data, columns=(data.keys()), index=['current'])


def convert_ld(data: List[Dict,]) -> DataFrame:
    temp = convert_ld_to_dict(data)
    return DataFrame(temp, columns=list(temp.keys()))


def convert_lo(data: List[Any,], index: str = "datetime") -> DataFrame:
    temp = convert_lo_to_dict(data)
    if temp.get(index) is None:
        return DataFrame()
    return DataFrame(temp, columns=list(temp.keys()), index=temp[index])


if __name__ == '__main__':
    te = [
        {
            "hello": 1,
            "thank": 2,
            "go": 1
        },
        {
            "hello": 1,
            "thank": 5,
            "go": 1
        },
        {
            "hello": 3,
            "thank": 2,
            "go": 1
        },
        {
            "hello": 1,
            "thank": 2,
            "go": 3
        },
    ]
    d = convert_position_holding(data=te)
    print(d.items)
