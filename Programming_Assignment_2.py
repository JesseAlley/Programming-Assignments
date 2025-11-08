#4.1
print("\n4.1")
secret = 4
guess = int(input("Choose a number between 1 and 10\n"))

if(guess < secret):
    print("Too low")
elif(guess == secret):
    print("Just right")
else:
    print("Too high")

#4.2
print("\n4.2")
small = False
green = True

if(green):
    print("Green: pea, watermelon")
else:
    print("Not green: cherry, pumpkin")
if(small):
    print("Small: cherry, pea")
else:
    print("Not small: watermelon, pumpkin")

#6.1
print("\n6.1")
nums = [3,2,1,0]
for num in nums:
    print(num)

#6.2
print("\n6.2")
guess_me = 7
var_num = 1

while(var_num != guess_me):
    print(var_num)
    if(var_num < guess_me):
        print("Too low")
        var_num += 1
    elif(var_num > guess_me):
        print("Oops")
        break
    elif(var_num == guess_me):
        break
print(var_num)
print("Found it!")

#6.3
print("\n6.3")

guess_me = 5
var_num = 0
for num in range(10):
    print(var_num)
    if(var_num < guess_me):
        print("Too low")
        var_num += 1
    elif(var_num > guess_me):
        print("Oops")
        break
    elif(var_num == guess_me):
        print("Found it!")
        break