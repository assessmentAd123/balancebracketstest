# Python3 program to check for
# balanced brackets.

# function to check if
# brackets are balanced


def balanced(input_par):
	stack = []

	for char in input_par:
		if char in ["(", "{", "["]:
			stack.append(char)
		else:
			# IF it's not opening it must close 
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False
	# if empty
	if stack:
		return False
	return True


#Example:
#Input: "((()))"
#Output: True
#Input: "[()]{}"
#Output: True
#Input: "({[)]"
#Output: False

if __name__ == "__main__":
	ptest_string = "((()))"

	# Function call
	if balanced(ptest_string):
		print("True")
	else:
		print("False")
	ptest_string = "[()]{}"
	# Function call
	if balanced(ptest_string):
		print("True")
	else:
		print("False")

	ptest_string = "({[)]"
	# Function call
	if balanced(ptest_string):
		print("True")
	else:
		print("False")

# This code is contributed by AnkitRai01 and improved
# by Raju Pitta
