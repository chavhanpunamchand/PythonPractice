from abc import ABC,abstractmethod

class employeesService(ABC):

    @abstractmethod
    def addEmployees(self,emp):
        pass

    @abstractmethod
    def getEmployees(self,empid):
        pass

    @abstractmethod
    def updateEmployees(self,empid,values):
        pass

    @abstractmethod
    def deleteEmployees(self,empid):
        pass

    @abstractmethod
    def getAllEmployees(self):
        pass

    @abstractmethod
    def getEmployeesOnRole(self,role):
        pass



