from Point import Point
from data import Price, Rectangle, Circle, Book, Employee
import unittest
import math

from hw1 import vowel_count, short_lists, ascending_pairs, add_prices, rectangle_area, circle_bound, books_by_author, \
    below_pay_average


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count(self):
        input_list = "Hello World"
        result = vowel_count(input_list)
        expected = 3
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists(self):
        input_list = [[1, 2], [3], [4, 5, 6], [8, 7]]
        result = short_lists(input_list)
        expected = [[1,2], [8,7]]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs(self):
        input_list = [[1, 2], [3], [4, 5, 6], [8, 7]]
        result = ascending_pairs(input_list)
        expected = [[1, 2], [3], [4, 5, 6], [7, 8]]
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices(self):
        price1 = Price(5, 75)
        price2 = Price(3, 50)
        price3 = add_prices(price1, price2)
        expected = Price(9,25)
        self.assertEqual(expected, price3)

    # Part 5
    def test_rectangle_area(self):
        top_left = Point(1,4)
        bottom_right = Point(5,1)
        rec1 = Rectangle(top_left, bottom_right)
        result = rectangle_area(rec1)
        expected = 12
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author(self):
        book1 = Book(["J.K. Rowling"], "Harry Potter and the Goblets Fire")
        book2 = Book(["J.K. Rowling"], "Harry Potter and the Deathly Hallows")
        book3 = Book(["Rick Riordan"], "Percy Jackson and the Lightning Thief")
        book4 = Book(["Rick Riordan"], "Percy Jackson and the Last Olympian")

        list1 = [book1, book2, book3, book4]

        rowling = books_by_author("J.K. Rowling", list1)
        expected_rowling = [Book(['J.K. Rowling'], 'Harry Potter and the Goblets Fire'), Book(['J.K. Rowling'], 'Harry Potter and the Deathly Hallows')]
        self.assertEqual(expected_rowling, rowling)

        riordan = books_by_author("Rick Riordan", list1)
        expected_riordan = [Book(['Rick Riordan'], 'Percy Jackson and the Lightning Thief'),
                            Book(['Rick Riordan'], 'Percy Jackson and the Last Olympian')]
        self.assertEqual(expected_riordan, riordan)

    # Part 7
    def test_circle_bound(self):
        rec1 = Rectangle(Point(1, 5), Point(4, 1))
        bounding_circle = circle_bound(rec1)
        center_x = (1+4) / 2
        center_y = (5+1) / 2
        expected_circle = Point(center_x, center_y)
        radius = math.sqrt((center_x-1) **2 + (center_y-5) **2)
        expected = Circle(expected_circle,radius)
        self.assertEqual(expected, Circle(expected_circle, radius))

    # Part 8
    def test_below_pay_average(self):
        employees = [
            Employee("Ramya", 5000),
            Employee("Kamala", 4500),
            Employee("Heather", 5500),
            Employee("Erik", 4700)
        ]
        result = [below_pay_average(employees)]
        expected = ['Kamala', 'Erik']


if __name__ == '__main__':
    unittest.main()
