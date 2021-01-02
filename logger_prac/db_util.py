import pymysql


def get_connection():
    try:
        return pymysql.connect('localhost','root','root','pydb')
    except BaseException as e:
        print(e.args)

def close_resources(conn,cursor):
    try:
        if cursor:
            cursor.close()
    except BaseException as e:
        print(e.args)

    try:
        if conn:
            #conn.commit()
            conn.close()
    except BaseException as b:
        print(b.args)