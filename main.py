from models import *


if __name__ == "__main__":
    print("Hello")
    print(Preciptation.query())
    print(Inundation.query())
    print(LunarPhase.position())

    for prec in Preciptation.query():
        print(prec.date, prec.value)
