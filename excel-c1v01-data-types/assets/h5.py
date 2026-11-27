# why long IDs must stay text: a number keeps about 15 digits (Microsoft documents 15 digits of precision)
x=1234567890123456789
print("the id as written    :", x)
print("the id stored as float:", int(float(x)))
print("same digits?          :", x==int(float(x)))
print("as text it stays      :", str(x))
