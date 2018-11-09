#!/usr/bin/env python3

def calculate(arg):
	stack = []

	tokens = arg.split()

	for token in tokens:
		try:
			stack.append(int(token))
		except ValueError:
			skip = 0
			val2 = stack.pop()
			if token == '~':
				skip = 1
				result = ~val2
			if skip == 0:
				val1 = stack.pop()
				if token == '+':
					result = val1 + val2
				elif token == '-':
					result = val1 - val2
				elif token == '/':
					result = val1 / val2
				elif token == '%':
					result = (val1 * val2) / 100
				elif token == '&':
					result = val1 & val2
				elif token == '|':
					result = val1 | val2
				elif token == '^':
					result = 1
					for x in range(val2):
						result = result * val1
					
			stack.append(result)

	if len(stack) > 1:
		raise ValueError('Too many arguments!')

	return stack[0]

def main():
	while True:
		try:
			result = calculate(input('rpn calc> '))
			print(result)
		except ValueError:
			pass

if __name__ == '__main__':
	main()
