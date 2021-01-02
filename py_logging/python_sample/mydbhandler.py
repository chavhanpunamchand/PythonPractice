import logging
from py_logging.python_sample.db_util import get_connection
'''
CREATE TABLE APP_LOGS(
    log_id int,
    level_name varchar(30),
    message varchar(256),
    line_no int,
    created_at varchar(256),
    fun_name varchar(30),
    primary key(log_id)
)

insert into app_logs values(101,'INFO','THis is info message',33,'2021-01-02 10:03:55,075','m1');


insert into app_logs values({},'{}','{}',{},'{}','{}');
'''


def myapp_gen():
    cnt = 100
    while True:
        cnt = cnt + 1
        yield cnt

gen = myapp_gen()

class MyDBHandler(logging.Handler):

    def emit(self, record):         # HANDLERS INTERNALLY CALLS TO EMIT--> LOGIC -- TO INSERT THE LOG INSIDE DB..
        message = record.message
        funname = record.funcName
        createdtime = record.asctime
        lname = record.levelname
        lnum = record.lineno
        try:
            sql = "insert into app_logs values({},'{}','{}',{},'{}','{}')".\
                format(next(gen),lname,message,lnum,str(createdtime),funname)
            print(sql)
            conn = get_connection()
            cursur = conn.cursor()
            cursur.execute(sql)
            conn.commit()
            cursur.close()
            conn.close()
        except:
             pass