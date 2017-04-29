import pymysql
import pymysql.cursors


def connect():
    conn = pymysql.connect(user='suricato', password='kirilenko',
                           host='suricato.ccuf5yniv7dz.sa-east-1.rds.amazonaws.com',
                           database='suricato')
    return conn


conn = connect()


def cursor(conn):
    return conn.cursor()


class Preciptation:
    def __init__(self, db_row):
        (self.date, self.city, self.value) = db_row
        # (date, city, value) = db_row
        # self.date = date

    def query(self):
        sql = 'SELECT precipitation.`date` , city.name, precipitation.quantity FROM suricato.precipitation INNER JOIN suricato.city ON city.pk_city = precipitation.fk_city'
        cur = cursor(conn)
        cur.execute(sql)
        cur.close()


results = []
for row in cur:
    print(type(row))
    (data, city, precip) = row
    print(city)

print(results)
cur.close()
conn.close()
