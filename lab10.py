def checkMod(module):
    match module:
        case "CSC1006":
            return "Mathematics II"
        case "CSC1007":
            return "Operating Systems"
        case "CSC1008":
            return "Data Structure and Algorithms"
        case "CSC1009":
            return "Object Oriented Programming"
        case "CSC1010":
            return "Computer Networks"    

print("Hello Glasgow")

x = input("Enter first number: ")
y = input("Enter second number: ")
avg = (float(x)+float(y))/2
print("The average is " + str(avg))

module = input("Enter module: ")
print(checkMod(module))

for i in range(102,65,-1):
    if(i % 2 != 0):
        print("Value of i is " + str(i))

