import db
import math, decimal, datetime


class BaseModel:
    @classmethod
    def find_all(cls, sql):
        with db.connect() as cur:
            cur.execute(sql)
            return [cls(row) for row in cur]


class Preciptation(BaseModel):
    def __init__(self, db_row):
        (self.date, self.city, self.value, self.level) = db_row
        # (date, city, value) = db_row
        # self.date = date

    @classmethod
    def query(cls):
        sql = 'SELECT precipitation.`date` , city.name, precipitation.quantity, precipitation.level FROM suricato.precipitation INNER JOIN suricato.city ON city.pk_city = precipitation.fk_city'
        return cls.find_all(sql)


class Inundation(BaseModel):
    def __init__(self, db_row):
        (self.date, self.city) = db_row
        # (self.date, self.city) = date.date(), city
        # (date, city, value) = db_row
        # self.date = date

    @classmethod
    def query(cls):
        sql = 'SELECT inundation.date_hour , city.name FROM suricato.inundation INNER JOIN suricato.city ON city.pk_city = inundation.fk_city'
        return cls.find_all(sql)


class LunarPhase:
    @classmethod
    def position(cls, now=None):
        if now is None:
            now = datetime.datetime.now()
        dec = decimal.Decimal
        diff = now - datetime.datetime(2001, 1, 1)
        days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
        lunations = dec("0.20439731") + (days * dec("0.03386319269"))
        lunations = lunations % dec(1)

        phasename = cls.phase(lunations)
        roundedpos = round(float(lunations), 3)
        return (phasename, roundedpos)

    def phase(pos):
        dec = decimal.Decimal
        index = (pos * dec(8)) + dec("0.5")
        index = math.floor(index)
        return {
            0: "New Moon",
            1: "Waxing Crescent",
            2: "First Quarter",
            3: "Waxing Gibbous",
            4: "Full Moon",
            5: "Waning Gibbous",
            6: "Last Quarter",
            7: "Waning Crescent"
        }[int(index) & 7]
