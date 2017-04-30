import pymysql
import pymysql.cursors


def connect():
    return pymysql.connect(user='suricato', password='kirilenko',
                           host='suricato.ccuf5yniv7dz.sa-east-1.rds.amazonaws.com',
                           database='suricato')


def cursor(conn):
    return conn.cursor()
