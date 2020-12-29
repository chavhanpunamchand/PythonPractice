from employees import employeesDetails

def get_user_input(idwant=False):
    eid=0
    if idwant:
        print("Value add operations")
        eid=int(input("Enter the employees ID: "))
    else:
        print("Add another values for update operation")
    ename=input("Enter name: ")
    eage=int(input("Enter Age: "))
    esalary=float(input("Enter salary: "))
    erole=input("Enter Role: ")

    return employeesDetails(eid,ename,eage,esalary,erole)

# get_user_input(idwant=True)
# print(employeesDetails())


