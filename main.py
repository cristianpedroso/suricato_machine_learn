from models import *
from analysis.basic import BasicAnalysis
from datetime import date

if __name__ == "__main__":
    print("Hello")
    preciptation = Preciptation.query()
    inundation = Inundation.query()
    lunarPhase = LunarPhase.position()

    BasicAnalysis.run(preciptation,inundation,datetime.datetime(1982,4,1,0,0,0))
