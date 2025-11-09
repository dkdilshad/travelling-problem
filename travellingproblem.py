name=input("Enter your name:")
distance=float(input("Enter the distance(in km):"))
vehicle=int(input("choose the vehicle type (bike (1) car (2) bus (3)):"));
price=1
p=0
disc=0

def pricecalcbike(d):
    if d<=50:
        price=d*5
    elif d<=200:
        price=d*4
    else:
        price=d*3.5
    return price

def pricecalccar(d):
    if d<=50:
        price=d*10
    elif d<=200:
        price=d*9
    else:
        price=d*8
    return price

def pricecalcbus(d):
    if d<=50:
        price=d*8
    elif d<=200:
        price=d*7
    else:
        price=d*6
    return price


if vehicle == 1:
    p=pricecalcbike(distance)
elif vehicle == 2:
    p=pricecalccar(distance)
elif vehicle == 3:
    p=pricecalcbus(distance)
else:
    print("choice not available!!")

print("passenger name:",name)
print("vehicle type:",vehicle)
print("Distance:",distance,"km")
print("Base Fare:",p,"₹")
if p>1500:
    disc=p*0.05
    print("Discount(5%):",disc,"₹")
print("Total amount payable:",p-disc,"₹")
if distance>500:
    print("suggestion: It's better to travel by train or flight for long distances.")
