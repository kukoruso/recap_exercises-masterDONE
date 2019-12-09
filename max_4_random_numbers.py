import random
print("This program generates 4 random numbers than prints the biggest one")
a = random.random()*100
b = random.random()*100
c = random.random()*100
d = random.random()*100

print("I have generated these numbers: %.2f %.2f %.2f %.2f" % (a, b, c, d))
if a >= b and a >= c and a >= d:
    print("The biggest number is %.2f" % a)
elif b >= a and b >= c and b >= d:
    print("The biggest number is %.2f" % b)
elif c >= a and c >= b and c >= d:
    print("The biggest number is %.2f" % c)
else:
    print("The biggest number is %.2f" % d)

# determine the second largest number
if b > a > c >= d:
    print("The 2nd biggest number is %.2f" % a)
elif a > b > c and b > d:
    print("The 2nd biggest number is %.2f" % b)
elif a > c > b and c > d:
    print("The 2nd biggest number is %.2f" % c)
else:
    print("The 2nd biggest number is %.2f" % d)
