values = [1, 2, "Rahul", 6, 9.0]

print(values[1])
print(values[-1])
print(values[1:4])

values.insert(3, "Shetty")

print(values)

values.append("LastElement")
print(values)
values[2] = "RAHUL"
print(values)

del values[0]

print(values)


tupleVariable = (1, 2, "Sid", 5.6)
print(tupleVariable)

print(tupleVariable[1])
#tupleVariable[2] = "Kiran"

DictionaryVariable = {1 : "Sid", "Kiran": 2}
print(DictionaryVariable)

print(DictionaryVariable["Kiran"])

dict = {}

dict["FirstName"] = "Shubh"
dict["LastName"] = "Mathur"

print(dict)
print(dict["LastName"])