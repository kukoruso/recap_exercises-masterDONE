num_read = 0
print("This program reads 4 numbers and will print the biggest one")
request = "Give me a number that you want to compare"
error = "That was not a valid number"
max = 4
while num_read < 7:
    try:
        read_line = input(request)
        num = float(read_line)
    except ValueError:
        print(error)
        continue
    if num_read == 0:
        max = num
    elif num > max:
        max = num
    num_read += 1

print("The biggest number read was ", max)

#change for max N numbers, where N is a number typed by the user

list1 = []
num = int(input("Enter number of numbers to compare: "))

for i in range(1, num + 1):
    ele = int(input("Enter number: "))
    list1.append(ele)

print("Largest number is:", max(list1))