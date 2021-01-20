'''
4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''

radius=float(input("Enter the radius of circle :"))
pie_value=3.141592653589793238
area_of_circle=pie_value* radius**2

print("The area of circle is :",area_of_circle)