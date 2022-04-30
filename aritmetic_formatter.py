def only_digits(problem):
	return (problem[0].isnumeric() and problem[2].isnumeric())

def check_sign(sign):
	return sign[1] if sign[1] == '+' or sign[1] == '-' else 0

def bigger(num1,num2):
	return len(num1) if len(num1) > len(num2) else len(num2)

def relist(problems):
	problems_handled = []
	for problem in problems:
		new_problem = problem.split()
		sign = check_sign(new_problem)
		if (only_digits(new_problem)):
			if (sign):
				problems_handled.append(new_problem)
			else:
				return "Error: Operator must be '+' or '-'."
		else:
			return "Error: Numbers must only contain digits."
	return problems_handled

def chek_errors(problem_list):
	if (len(problem_list) > 5):
		return "Error: Too many problems."
	relisted = relist(problem_list)
	if (type(relisted) != list):
		return relisted
	for item in relisted:
		bignum = bigger(item[0], item[2])
		if (bignum > 4):
			return "Error: Numbers cannot be more than four digits."
	return "ok"

def arithmetic_arranger(arithmetic_list, condition=False):
	up_line = []
	botton_line = []
	dash_line = []
	keep_result = ''
	result_line = []
	error = chek_errors(arithmetic_list)
	if (error != "ok"):
		return error
	relisted = relist(arithmetic_list)
	for neo_problem in relisted:
		big = bigger(neo_problem[0], neo_problem[2])
		sign = check_sign(neo_problem)
		up_line.append(f"{((big - len(neo_problem[0])) + 2) * ' '}{neo_problem[0]}")
		botton_line.append(f"{sign}{((big - len(neo_problem[2])) + 1) * ' '}{neo_problem[2]}")
		dash_line.append(f"{(big + 2) * '-'}")
		if (sign == '+'):
			keep_result = int(neo_problem[0]) + int(neo_problem[2])
		else:
			keep_result = int(neo_problem[0]) - int(neo_problem[2])
		result_line.append(f"{((big - len(str(keep_result))) + 2) * ' '}{str(keep_result)}")

	arranged_problems = f"{'    '.join(up_line)}\n{'    '.join(botton_line)}\n{'    '.join(dash_line)}"
	if (condition == True):
		arranged_problems = f"{'    '.join(up_line)}\n{'    '.join(botton_line)}\n{'    '.join(dash_line)}\n{'    '.join(result_line)}"

	return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print("\n")
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

