


from enum import Enum

class OrderEnum(Enum):
    SUCCESS = "SUCCESS"
    EXCEPTION = "EXCEPTION"





if __name__ == '__main__':
    print OrderEnum("SUCCESS")
    print OrderEnum.SUCCESS