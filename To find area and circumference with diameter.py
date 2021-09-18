"""def area(d):
    return 1/4 * 3.14 * (d*d)

def cr(d):
    return 3.14*d

print("please select operation -\n"
          "1. Find Area of Circle\n"
          "2. Find circumference Circle\n")
select = float(input("select operation form 1, 2 :"))


number_1 = float(input("Enter the circle's Diameter: "))
if select==1:
    print("The Area is ",area(number_1))

else:
    print("The circumference  is ", cr(number_1))
    """
# second method
pi=3.14
num=int(input("Enter the radius"))
area= pi*num*num
cirumfrence= 2*pi*num
print(area)
print(cirumfrence)

