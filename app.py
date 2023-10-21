"""
	Використання бібліотеки icecream
"""

from icecream import ic


def get_number_square_of(number:"Число"):
	"""Ого, та тут так скл
	адно!"""
	return number * number


# Тессстування
num1 = ic(get_number_square_of(10))
num2 = ic(get_number_square_of(5))
num3 = ic(get_number_square_of(9))

for elem in range(20):
	if elem == 4:
		ic()
	elif elem == 10:
		ic()
	elif elem == 200:
		ic() # Тут умова не буде відробляти.