#Operators
a = 3
a += 5 #var a operating on itself
print(f"{a = }")
b = 9 % 3 #modulo
c = 9 % 2
print(f"{9 % 3 = }")
print(f"9 % 3 = {b}") #equivalent to above
print(f"{7 % 2 = }")
#Condition
s = 8
print(f"\n{s = }")
print(f"{s > 7 & s < 20 = }")
print(f"{7 < s < 20 = }")
print(f"{not s != 8 = }") #double not condition
print(f"{s < 20 or s > 40 = }") # "or" can also be "|"
volleyball = True
football = True
tennis = False
print(f"{volleyball & (football | tennis) =  }")

#Data Types
d = 100_000_000
print(f"\n100_000_000 is: {type(d)}")
num1 = int("300")
print("int(\"300\")", type(num1))
str_conv = str(400)
print(f"str(400) {type(str_conv)}")
num2 = float("439.234")
print(f"float(\"439.234\"){type(num2)}")

#Booleans
a = True; print(type(a))
b = False; print(type(b))
print(1==True)
print(1 == False)
