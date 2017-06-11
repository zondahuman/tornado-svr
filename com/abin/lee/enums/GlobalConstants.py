


from enum import Enum

class OrderEnum(Enum):
    SUCCESS = "SUCCESS"
    EXCEPTION = "EXCEPTION"
    INIT = "INIT"
    ERROR = "ERROR"


class MessageEnum(Enum):
    SUCCESS = "SUCCESS"
    EXCEPTION = "EXCEPTION"
    INIT = "INIT"
    ERROR = "ERROR"




if __name__ == '__main__':
    print OrderEnum("SUCCESS")
    print OrderEnum.SUCCESS