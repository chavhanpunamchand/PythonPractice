from abc import ABC,abstractmethod
from helper import *
from service import employeesService

CREATE_TABLE_SQL='''CREATE TABLE emp_info(emp_id int NOT NULL AUTO_INCREMENT,emp_name varchar(45) NOT NULL,emp_age int NOT NULL,emp_salary float NOT NULL,emp_role varchar(50) NOT NULL,	
		PRIMARY KEY (emp_id));'''
INSERT_RECORD_SQL='''insert into emp_info values({},"{}",{},{},"{}");'''
UPDATE_RECORD_SQL='''UPDATE emp_info SET emp_name='{}',emp_age={},emp_salary='{}',emp_role='{}' WHERE emp_id = {};'''
DELETE_RECORD_SQL='''delete from emp_info where emp_id={};'''
GET_ALL_RECORD_SQL='''select * from emp_info'''
GET_SINGLE_RECORD_SQL='''select * from emp_info where emp_id={};'''
GET_RECORD_ON_EMP_ROLE_SQL='''select * from emp_info where emp_role="{}";'''

Database_queries={
    'CREATE_TABLE':CREATE_TABLE_SQL,
    'INSERT_RECORD':INSERT_RECORD_SQL,
    'UPDATE_RECORD':UPDATE_RECORD_SQL,
    'DELETE_RECORD':DELETE_RECORD_SQL,
    'GET_ALL_RECORD':GET_ALL_RECORD_SQL,
    'GET_SINGLE_RECORD':GET_SINGLE_RECORD_SQL,
    'GET_RECORD_ON_EMP_ROLE':GET_RECORD_ON_EMP_ROLE_SQL
}
import pymysql

def get_database_connection():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='root', database='emp_info', port=3306)
        return conn
    except BaseException as b:
        print(type(b))


def establish_comm_channel(sql):# to pass sql/data/retrive--> from/db -- datbase-python
    conn = None     # local variable
    channel = None  # local variable        #conn --> pysql             --> cursor --> conn         --> sql--> cursor
    try:
        conn = get_database_connection()    # db ack-- handshaking-- with database
        channel = conn.cursor()             # thru ack- communication channel --> database sql
        channel.execute(sql)                # will run sql on datbase-->
    except :
        print("problem in query execution")
    else:
        conn.commit()
        return True     #operation successful..    deemed -- not an immediate impact--[try-->except--]     blocks la-->
    finally:
        if channel:
            channel.close()
        if conn:
            conn.close()

def retrive_data_from_db(sql,many=True):
    conn = None  # local variable
    channel = None  # local variable        #conn --> pysql             --> cursor --> conn         --> sql--> cursor
    try:
        conn = get_database_connection()  # db ack-- handshaking-- with database
        channel = conn.cursor()  # thru ack- communication channel --> database sql
        channel.execute(sql)  # will run sql on datbase-->
        if many:
            return channel.fetchall()           # all records
        else:
            return channel.fetchone()           # fetch one
    except:
        print("problem in data fech")
    else:
        conn.commit()
    finally:
        if channel:
            channel.close()
        if conn:
            conn.close()






class employessDBOp(employeesService):

    def create_table_for_employees(self):
        create_table=Database_queries['CREATE_TABLE']
        establish_comm_channel(create_table)
        print("Table created......")

    def addEmployees(self, emp):
        insert_table=Database_queries['INSERT_RECORD']
        insert_table=insert_table.format(emp.empID,emp.empName,emp.empAge,emp.empSalary,emp.empRole)
        print(insert_table)
        result=establish_comm_channel(insert_table)
        if result:
            print("Employees add successful")



    def getAllEmployees(self):
        get_all_record = Database_queries['GET_ALL_RECORD']
        print(get_all_record)
        # allRecord=establish_comm_channel(get_all_record)
        # print(allRecord)
        rows=retrive_data_from_db(get_all_record,many=True)

        empList=[]
        for row in rows:
            empList.append(employeesDetails(eid=row[0],ename=row[1],eage=row[2],esalary=row[3],erole=row[4]))
        return empList

        # print("Getting all record sucessfully...")

    def deleteEmployees(self,empID):
        delete_Record = Database_queries['DELETE_RECORD']
        delete_Record=delete_Record.format(empID)
        print(delete_Record)
        establish_comm_channel(delete_Record)
        print("Record deleted Successfully........")

    def getEmployees(self,empid):
        get_single_record = Database_queries['GET_SINGLE_RECORD']
        get_single_record=get_single_record.format(empid)
        print(get_single_record)
        # allRecord=establish_comm_channel(get_all_record)
        # print(allRecord)
        rows=retrive_data_from_db(get_single_record,many=False)

        empList=[]
        for row in rows:
            empList.append(employeesDetails(eid=rows[0],ename=rows[1],eage=rows[2],esalary=rows[3],erole=rows[4]))
        return empList


    def getEmployeesOnRole(self,emp_role):
        get_emp_based_on_role = Database_queries['GET_RECORD_ON_EMP_ROLE']
        get_emp_based_on_role = get_emp_based_on_role.format(emp_role)
        print(get_emp_based_on_role)
        # allRecord=establish_comm_channel(get_all_record)
        # print(allRecord)
        rows = retrive_data_from_db(get_emp_based_on_role, many=True)
        print(rows)
        empList = []
        for row in rows:
            empList.append(employeesDetails(eid=row[0],ename=row[1],eage=row[2],esalary=row[3],erole=row[4]))
        return empList


    def updateEmployees(self,empid,emp):
        dbemp=self.getEmployees(empid)
        if dbemp:
            update_record=Database_queries['UPDATE_RECORD']
            update_record=update_record.format(emp.empName,emp.empAge,emp.empSalary,emp.empRole,empid)
            print(update_record)#UPDATE emp_info SET emp_name='{}',emp_age={},emp_salary='{}',emp_role='{}' WHERE emp_id = {};
            result=establish_comm_channel(update_record)
            if result:
                print("Record update successful")
                print(dbService.getAllEmployees())
        else:
            print("Record not found")




if __name__ == '__main__':

    dbService=employessDBOp()

    # dbService.create_table_for_employees()
    # for item in range(5):
    emp=get_user_input(idwant=True)
    #     dbService.addEmployees(emp)
    # dbService.deleteEmployees(104)
    # print(dbService.getAllEmployees())
    # print(dbService.getEmployeesOnRole('SSE'))
    # values={ 'empName':'Punamchand','empAge':25,'empSalary':60000,'empRole':'SSE'}
    dbService.updateEmployees(emp.empID,emp)
