import db


class Preciptation:
    def __init__(self, db_row):
        (self.date, self.city, self.value) = db_row
        # (date, city, value) = db_row
        # self.date = date

    @classmethod
    def query(cls):
        sql = 'SELECT precipitation.`date` , city.name, precipitation.quantity FROM suricato.precipitation INNER JOIN suricato.city ON city.pk_city = precipitation.fk_city'

        with db.connect() as cur:
            cur.execute(sql)
            return [cls(row) for row in cur]

class Inundation:
    def __init__(self, db_row):
        (self.date, self.city) = db_row
        # (date, city, value) = db_row
        # self.date = date

    @classmethod
    def query(cls):
        sql = 'SELECT inundation.date_hour , city.name FROM suricato.inundation INNER JOIN suricato.city ON city.pk_city = inundation.fk_city'

        with db.connect() as cur:
            cur.execute(sql)
            return [cls(row) for row in cur]