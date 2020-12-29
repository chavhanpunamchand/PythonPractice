'''
Program to find the surface area of the cylinder
Explanation:
Surface Area of Cylinder = 2 Π  (r + h)
Here, r is the radius and h is the height of the cylinder.
	Π ( pi ) = 22/7 = 3.14
'''
def SurfaceAreaCylinder(r,h):
    pi=22/7
    return 2*pi*(r+h)


r=float(input("Enter the radius of cylinder: "))
h=float(input("Enter the height of cylinder: "))
print("Area of cylinder is: ",SurfaceAreaCylinder(r,h))