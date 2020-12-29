'''Structure of employees where you will add employees'''

class employeesDetails:

    def __init__(self,eid,ename,eage,esalary,erole):
        self.empID=eid
        self.empName=ename
        self.empAge=eage
        self.empSalary=esalary
        self.empRole=erole

    def __str__(self):
        return f'''\n Employee_ID: {self.empID} \n Employee_Name: {self.empName}\n Employees_Age: {self.empAge}\n Employees_salary: {self.empSalary}\n Employees_Role: {self.empRole}'''

    def __repr__(self):
        return str(self)


# print(employeesDetails(101,"Punamchand",26,25000.0,"SSE"))




