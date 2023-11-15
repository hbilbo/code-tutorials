#For loop similar to "map" result
songs = ["1.mp3","2.mp3","3.mp3"]
song_rn = lambda song: f"my_song_{song.split('.')[0]}.flac"
converted = []
for i in songs:
    converted.append(song_rn(i))
print(converted)

#*Some possible iterables in a for loop
iterable1 = [1,2,3,4]
iterable2 = "Hello World"
iterable3 = {"color": "blue", "shape": "round"}
iterable4 = map(song_rn,songs)
iterable5 = range(1,5)
number_sum = 0
for num in iterable1:
    number_sum += num
print(number_sum)
for letter in iterable2:
    print(letter)
my_list = []
for key in iterable3:
    my_list.append(iterable3[key])
print(my_list)

#Running fizz_buzz in loop
def fizz_buzz(num):
    if num % 3 == 0:
        if num % 15 == 0:
            return "fizzbuzz"
        else:
            return "fizz"
    elif num % 5 == 0:
        return "buzz"
    return num
fizzbuzz_number = []
for number in range(1,100+1):
    fn = fizz_buzz(number)
    fizzbuzz_number.append(fn)
# print(fizzbuzz_number)
#Can achieve same result using map
fizzbuzz_number2 = list(map(fizz_buzz, range(1, 100+1)))
# print(fizzbuzz_number2)

#Enumerate
dow = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for i, day in enumerate(dow):
    # print(a, end=',')
    print(f"{i} -> {day}")

#Stock return challenge
stock_prices = [3.4,3.5,3.2,2.8,3.9,4.1,3.3]
def max_profit(prices):
    profit = 0
    for i, val in enumerate(prices):
        if val > prices[i-1]:
            print(f"{prices[i-1]} -> {val}")
            profit += val - prices[i-1]
    return profit
print(max_profit(stock_prices))

#While loop
import random
target = 100_000
visitors = []
while sum(visitors) < target:
    day = random.randrange(300,10_000)
    visitors.append(day)
print(visitors); print(sum(visitors))

"""
List Comprehension - can store output of process in
a list directly from one line of code using for loop.
can also be done for dictionaries, etc.
"""
#Recall song_rn function
list_comp = [song_rn(x) for x in songs]
print(list_comp)
#Reverse key-value pairs in dictionary
my_dict = {1: "hello",2: "goodbye",3: "greetings"}
my_dict2 = {value: key for key, value in my_dict.items()}
print(my_dict); print(my_dict2)

#Recursion - Refers to when a function calls itself within
# the function
def countdown(n):
    if n > 0:
        print(n)
        countdown(n-1)
    else:
        print("Happy New Year!!")
countdown(10)
#This can also be done with a while loop
def countdown2(n):
    while n > 0:
        print(n)
        n -= 1
    print("Happy New Year!!")
countdown2(10)

#tqdm - progress bar
# import time
# from tqdm import tqdm
# pages = range(1,30)
# for page in tqdm(pages):
#     time.sleep(random.randrange(1, 10)/100)

#Challenge interview question
'''
Imagine we have a robot that picks items from a shelf. The robot
can go up(U), down(D), left(L), and right(R). Given a sequence of
movements (e.g. URDDL) determine if the robot has successfully
picked up the item from the shelf and returned to its original
position.
'''
def check_home(moves):
    x = y = 0
    for position in moves:
        if position == "U":
            y += 1
        if position == "D":
            y -= 1
        if position == "L":
            x -= 1
        if position == "R":
            x += 1
    print(x == 0 and y == 0)
    # item_list = [pos for pos in item_pos]
    # rob_list = [pos for pos in rob_mov]
    # print(item_list); print(rob_list)
    # n = len(item_list)
    # i = 0
    # while i < n:
    #     if rob_list[i] == item_list[i]:
    #         logical_check = True
    #     else:
    #         logical_check = False
    #         # return
    #     print(logical_check)
    #     i += 1
    # print(logical_check)
    # print("test")
robot_mov = "RLLUULRRDD"
check_home(robot_mov)