from models import *
from datetime import datetime, timedelta
from functools import reduce
import requests

class BasicAnalysis:
    def __init__(self):
        print("FOI")

    @classmethod
    def run(cls, preciptations, inundations,compare, days=7):
        global total_level
        total_rains = 0
        preciptations_count = 0
        lass_rain = 0
        for (i, inundation) in enumerate(inundations):
            inundation_date = inundation.date.date()
            print(f"\nSearching preciptations {days} days before {inundation_date}")
            rains = list(filter(lambda precip: precip.date <= inundation_date and precip.date >= (inundation_date - timedelta(days=days)), preciptations))
            print(f"{len(rains)} preciptations")

            if rains:
                total = reduce(lambda x, y: x+y, list(map(lambda x: x.value, rains)))
                total_level = reduce(lambda x, y: x + y, list(map(lambda x: x.level, rains)))
                average_rains = total/len(rains)
                avarage_level = total_level/len(rains)
                if total_rains < lass_rain:
                    lass_rain = total_rains
                print(f"Total rain quantity {total}")
                print(f"Average rain {average_rains} in {days} days")
                print(f"total_level {total_level}")
                print(f"Average level {avarage_level} in {days} days")
                print()
                total_rains += total
                preciptations_count += 1

        print(f"total inundations  {preciptations_count}")
        print(f"avarage rain {total_rains/preciptations_count}")

        inundation_date = compare.date()
        print(f"\nCompare - Searching preciptations {days} days before {inundation_date}")
        rainsC = list(filter(
            lambda precip: precip.date <= inundation_date and precip.date >= (inundation_date - timedelta(days=days)),
            preciptations))
        print(f"Compare - {len(rains)} preciptations")
        if rainsC:
            totalC = reduce(lambda x, y: x + y, list(map(lambda x: x.value, rainsC)))
            total_levelC = reduce(lambda x, y: x + y, list(map(lambda x: x.level, rainsC)))
            average_rainsC = totalC / len(rains)
            avarage_levelC = total_levelC / len(rains)
            print(f"Compare - Total rain quantity {totalC}")
            print(f"Compare - Average rain {average_rainsC} in {days} days")
            print(f"Compare - total_level {total_levelC}")
            print(f"Compare - Average level {avarage_levelC} in {days} days")
            print(lass_rain)
            if totalC >= lass_rain and total_levelC >= total_level:
                r = requests.get('https://f3e881bf.ngrok.io/alert')
                print(r)



