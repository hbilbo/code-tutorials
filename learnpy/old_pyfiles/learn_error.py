""" Types of Errors
IndexError
A = [1,2,3]
A[6]

SyntaxError
True 0 or "Name"

TypeError
"a" + 1

ValueError
float("34.567.986")

KeyError
dict = {"hola": "hello"}
dict["hello"]

IndentationError
def func:
    my_variable = 1
  return my_variable
"""

#try, except, and pass
# float("$5,987.32") -> ValueError
try:
    float("$5,987.32")
except:
    print("Can't do it")

def discount(price, by=0.2):
    try:
        price = price.replace("$","").replace(",","")
        price = float(price)
        return price * (1-by)
    except:
        return None
my_price = ("$5,987.32")
print("Discounted price:",discount(my_price))

#Raise error
def discount(price, by=0.2):
    if by >= 1:
        raise ValueError("Cannot discount more than 100%!")
    return price * (1-by)
print(discount(50,0.9))

#Warnings
import warnings
warnings.warn("Use .method2() instead of .method1()",DeprecationWarning)
print("This will still print")