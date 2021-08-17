from typing import Type


def singleton(__class: Type):
    def inner(*args):
        if not hasattr(__class, "instance"):
            setattr(__class, "instance", __class(*args))
        return getattr(__class, "instance")
    return inner
