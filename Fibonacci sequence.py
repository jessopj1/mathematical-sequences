import os
order = 1
value = 1
value2 = 0
print("This is John's Fibonacci number generator.")
print("Number in sequence = ", order)
print("Value = ", value)
value = int(value) + int(value2)
iterations = input("How many Fibonacci numbers would you like to generate? I suggest at least 100: ")
print("You chose to get the fisrt ", iterations, " Fibonacci numbers" )

while (order < int(iterations)):
    order = int(order) + 1
    prevvalue = value
    value = value + value2
    print("Value = ", value)
    value2 = prevvalue

print("That is the first ",iterations ," numbers of the Fibonacci sequence")
os.system("pause")
