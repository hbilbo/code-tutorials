#If statement
month = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]
print(month)
month = dict(list(zip(month, range(1,12+1)))); print(month)

current_month = "Jun"
month_number = month[current_month]
if month[current_month] in [1,2,3,4,5]:
    print("Basketball Season")
# If we use
# "elif month_number >= 6 & month_number <= 8:"
# here it won't work correctly due to autocasting.
# need to use () to separate conditions
elif (month_number >= 6) & (month_number <= 8):
    print("Off-Season")
else:
    print("Football Season")

"""
Fizzbuzz Challenge
If a number is:
    - Divisible by 3, return fizz
    - Divisible by 5, return buzz
    - Divisible by 15, return fizzbuzz
"""
def fizz_buzz(num):
    if num % 3 == 0:
        if num % 15 == 0:
            return "fizzbuzz"
        else:
            return "fizz"
    elif num % 5 == 0:
        return "buzz"
    return num
print(fizz_buzz(7))

def rock_paper_scissors(signal):
    if signal == "rock":
        return "paper"
    elif signal == "paper":
        return "scissors"
    elif signal == "scissors":
        return "rock"
print(rock_paper_scissors("scissors"))