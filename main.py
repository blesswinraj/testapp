"""Basic demo script for the testapp workspace.

Features:
- simple CLI prompts
- small numeric utility function

Run:
	python main.py
"""
from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
	"""Return the sum of a and b."""
	return a + b


def get_number(prompt: str) -> float:
	"""Prompt the user until a valid number is entered."""
	while True:
		val = input(prompt)
		try:
			return float(val)
		except ValueError:
			print("Please enter a valid number (e.g. 3.14 or 2).")


def main() -> None:
	print("Welcome to TestApp demo.")
	name = input("What's your name? ").strip() or "Friend"
	print(f"Hello, {name}!")

	a = get_number("Enter first number: ")
	b = get_number("Enter second number: ")
	result = add(a, b)

	# Print a friendly, nicely formatted result
	if a.is_integer() and b.is_integer():
		# show integers without trailing .0 when both inputs are integers
		print(f"{int(a)} + {int(b)} = {int(result)}")
	else:
		print(f"{a} + {b} = {result}")


if __name__ == "__main__":
	main()

