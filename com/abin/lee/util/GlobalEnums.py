
from enum import Enum

class HttpEnum(Enum):
    CONTENT_TYPE = "'content-type':'application/json charset=utf-8'"
    COOKIE = '"Cookie": "rules_session_id=64b713c52c7511e6a4519801a7928995"'
    SOURCE = '"RRDSource": "TL"'

class Animals(Enum):
    ant = 1
    bee = 2
    cat = 3
    dog = 4


class Color(Enum):
    red = 1
    red_alias = 1

if __name__ == '__main__':
    print HttpEnum.CONTENT_TYPE.value
    print Animals['ant']
    print Color['red']
    # print Color(2)
    red_member = Color.red
    print red_member.name
    print red_member.value