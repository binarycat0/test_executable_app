from .utils import date_with_offset


def now():
    print(date_with_offset())


def tomorrow():
    print(date_with_offset(1))


def yesterday():
    print(date_with_offset(-1))


def offset(offset):
    print(date_with_offset(offset))
