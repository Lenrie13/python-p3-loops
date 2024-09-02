#!/usr/bin/env python3

def happy_new_year():
    count = 10

    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")

happy_new_year()


def square_integers(int_list):
    squared_list = []

    for i in int_list:
        i_squared = i * i
        squared_list.append(i_squared)

    return squared_list

print(square_integers([3, 4, 5, 6, 7, 8, 9]))


def fizzbuzz():
    for i in range(1, 101): 
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")  
        elif i % 3 == 0:
            print("Fizz")  
        elif i % 5 == 0:
            print("Buzz")  
        else:
            print(i)

fizzbuzz()
