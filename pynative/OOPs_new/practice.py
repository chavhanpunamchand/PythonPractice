"""
check the instance class of the vehicle class
"""

class Vehicle:

    def __init__(self,name,max_speed,mileage,capacity):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        self.capacity=capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount=super().fare()
        amount += amount * 10/100
        return amount

school_bus=Bus(name="Little volvo",max_speed=180,mileage=14,capacity=50)
# print("School bus color:",school_bus.color,"Vehicle name:",school_bus.name,"Speed:",school_bus.max_speed,"Mileage:",school_bus.mileage)
# print(school_bus.seating_capacity())
print("Total bus fare is :",school_bus.fare())
print(type(school_bus))
print(isinstance(school_bus,Vehicle))



import sys
sys.exit(0)
"""
Determine which class a given Bus object belong to (check type of a object)
"""

class Vehicle:

    def __init__(self,name,max_speed,mileage,capacity):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        self.capacity=capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount=super().fare()
        amount += amount * 10/100
        return amount

school_bus=Bus(name="Little volvo",max_speed=180,mileage=14,capacity=50)
# print("School bus color:",school_bus.color,"Vehicle name:",school_bus.name,"Speed:",school_bus.max_speed,"Mileage:",school_bus.mileage)
# print(school_bus.seating_capacity())
print("Total bus fare is :",school_bus.fare())
print(type(school_bus))


"""
 create a child class Bus that will inherit all of the variables and methods of the vehicle class
 define property that should have same value for every class instance
 add fare method
 """

class Vehicle:

    def __init__(self,name,max_speed,mileage,capacity):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        self.capacity=capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount=super().fare()
        amount += amount * 10/100
        return amount

school_bus=Bus(name="Little volvo",max_speed=180,mileage=14,capacity=50)
# print("School bus color:",school_bus.color,"Vehicle name:",school_bus.name,"Speed:",school_bus.max_speed,"Mileage:",school_bus.mileage)
# print(school_bus.seating_capacity())
print("Total bus fare is :",school_bus.fare())


"""
 create a child class Bus that will inherit all of the variables and methods of the vehicle class
 define property that should have same value for every class instance
 """

class Vehicle:
    # class attribute
    color="White"

    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

    # def seating_capacity(self,capacity):
    #     return f"The seating capacity of a {self.name} is {capacity} passanger"

class Bus(Vehicle):
    pass
    # def seating_capacity(self, capacity=50):
    #     return super().seating_capacity(capacity=50)

class Car(Vehicle):
    pass

school_bus=Bus(name="Little volvo",max_speed=180,mileage=14)
print("School bus color:",school_bus.color,"Vehicle name:",school_bus.name,"Speed:",school_bus.max_speed,"Mileage:",school_bus.mileage)
# print(school_bus.seating_capacity())



"""
 create a child class Bus that will inherit all of the variables and methods of the vehicle class
 """

class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(Vehicle):
    pass

school_bus=Bus(name="Little volvo",max_speed=180,mileage=14)
print("Vehicle name:",school_bus.name,"Speed:",school_bus.max_speed,"Mileage:",school_bus.mileage)
