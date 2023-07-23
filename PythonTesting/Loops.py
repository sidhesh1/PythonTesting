greeting = "Good Morning"

if greeting == "morning":
    print("Condition don't match")
else:
    print("Condition matches")
print("if else conditon completed")

#For loop

print("For Loop Example")
obj = [1, 2, 3, 4, 5, 6]
for i in obj:
    print(i)
print("------------------------------------")
sum = 0
for j in range(1, 6):
    sum = sum + j
print(sum)

print("------------------------------------")

for k in range(1, 10, 2):
    print(k)

print("------------------------------------")

for m in range(10):
    print(m)

#While Loop

print("---------------------While Loop-------------------")

it = 4

while it>1:
    print(it)
    it = it - 1
print("While condition is done")

print("-------------------------")

it = 4

while it>1:
    if it != 3:
        print(it)
    it = it-1
print("while loop executed")

print ("-------------------Continue and Break Statements")

it = 10;

while it > 1:
    if it == 9:
        it = it -1
        continue
    if it == 3:
        break
    print(it)

    it = it - 1