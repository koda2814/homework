"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""

class SimplifiedEnumMeta(type):
    def __init__(cls, name, bases, attrs):
        keys = getattr(cls, '_keys')
        for key in keys:
            setattr(cls, key, key)
        super().__init__(name, bases, attrs)


class SimplifiedEnum(metaclass=SimplifiedEnumMeta):
    _keys = ("RED", "BLUE", "ORANGE", "BLACK")


class ColorsEnum(SimplifiedEnum):
    pass


class SizesEnum(SimplifiedEnum):
    _keys = ("XL", "L", "M", "S", "XS")

assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"