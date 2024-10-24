from data import Price, Rectangle, Point, Book, Circle, Employee

import math

# Write your functions for each part in the space below.

# Part 1
#Counts the number of vowels in a given string
#input: a string
#output: an integer that sums up the number of vowels
def vowel_count(vowel: str) -> int:
    possible = "aeiouAEIOU"
    count = 0
    for char in vowel:
        if char in possible:
            count += 1
    return count

# Part 2
#Creates a list of all the short lists
#input: a nested list with lists of integers
#output: a nested list with lists of integers
def short_lists(list1: list[list[int]]) -> list[list[int]]:
    short = []
    for nList in list1:
        if len(nList) == 2:
            short.append(nList)
    return short

# Part 3
#Reorder the short lists in a nested list to make them in ascending order
#input: a nested list with lists of integers
#output: a nested list with lists of integers
def ascending_pairs(list1: list[list[int]]) -> list[list[int]]:
    result = []
    for nlist in list1:
        if len(nlist) == 2:
            if nlist[0] <= nlist[1]:
                result.append(nlist)
            else:
                nlist = [nlist[1], nlist[0]]
                result.append(nlist)
        else:
            result.append(nlist)
    return result

# Part 4
#Calculates the total price given two prices
#input: two Price objects
#output: Price object
def add_prices(price1: Price, price2: Price) -> Price:
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents
    if total_cents > 99:
        total_dollars += total_cents // 100
        total_cents = total_cents % 100
    return Price(total_dollars, total_cents)

# Part 5
#Calculates the area of a rectangle
#input: One rectangle object
#output: an integer for the total area calculation
def rectangle_area (rec1:Rectangle) -> int:
    width = rec1.bottom_right.x - rec1.top_left.x
    height = rec1.top_left.y - rec1.bottom_right.y

    return int(width * height)

# Part 6
#Creates a list of all the books in a list written by a certain author
#input: a string for the author name, a list of books
#outout: a list of books written by the author
def books_by_author(author:str, list1: list[Book]) -> list[Book]:
    return [book for book in list1 if author in book.authors]

# Part 7
#Creates the smallest possible circle that bounds a rectangle
#input: a rectangle object
#output: a circle object
def circle_bound(rec1: Rectangle) -> Circle:
    center_x = (rec1.top_left.x + rec1.bottom_right.x)/2
    center_y = (rec1.top_left.y + rec1.bottom_right.y)/2
    center = Point(center_x, center_y)

    radius = math.sqrt(((center_x - rec1.top_left.x) ** 2) + (center_y - rec1.top_left.y) ** 2)

    return Circle(center, radius)

# Part 8
#Creates a list of all the employees that are paid less than the average of all employees
#input: a list of all employees
#output: a list of all employees paid less than average
def below_pay_average(list1: list[Employee]) -> list[str]:

    if not list1:
        return []

    total_pay = sum(employee.pay_rate for employee in list1)
    average_pay = total_pay/len(list1)
    below_average = [employee.name for employee in list1 if employee.pay_rate < average_pay]
    return below_average



