# For Loop

# Cities = ["Pune", "Dublin", "Solapur"]
# for x in Cities:
#     print(x)

# for x in "Cities": # "for loop" for string var which prints sigle letter on new line and iterates
#     print(x)

# for x in range(5): # range(start, end, incrment) -> (0,5,1)
#     print(x)

# for x in range(10,20): # (10,20,1)
#     print(x)

# for x in range(10,20,2): # (10,20,2) -> incrementing it by 2
#     print(x)

# for x in range(10,20): # (10,20,1)
#     print(x)
# else:
#     print("Done!")

# for x in range(10,20):
#     pass

'''Display Fibonacci series up to 10 terms
    The Fibonacci Sequence is series of numbers
    The next number is found by adding up the two numbers before it'''

# num1 = 0
# num2 = 1
# num3 = int(input("Number of terms: "))
# print("Fibonacci Series of " + str(num3) + " terms is: ")
# for n in range(0, num3):
#     if(n <= 1):
#         next = n
#     else:
#         next = num1 + num2
#         num1 = num2
#         num2 = next
#     print(next, end = " ") # end parameter is for avoinding new line after executing one iteration of loop, 
#                            # so it will just give a blank space

# Cities = ["Pune", "Dublin", "Chennai", "Solapur"]
# for x in Cities:
#     print(x)
#     if x == "Chennai":
#         break

# Cities = ["Pune", "Dublin", "Chennai", "Solapur"]
# for x in Cities:
#     if x == "Chennai":
#         break
#     print(x)

# Cities = ["Pune", "Dublin", "Chennai", "Solapur"]
# for x in Cities:
#     if x == "Chennai":
#         continue
#     print(x)


