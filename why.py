def arithmetic_arranger(problems, arg=None):
  line_1 = str()
  line_2 = str()
  line_3 = str()
  result = str()

  #Evaluate number of problems
  if len(problems) > 5:
    error_1 = "Error: Too many problems."
    return error_1
  #Evalute each problem
  for problem in problems:
    #Evaluate if problem is addition or substraction
    if problem.find("*") > 0 or problem.find("/") > 0:
      error_2 = "Error: Operator must be '+' or '-'."
      return error_2
    #Evaluate if numbers in problem are numbers
    split_problem = problem.split()
    number_1 = split_problem[0]
    op_sign = split_problem[1] + " "
    number_2 = split_problem[2]
    space = "    "
    try:
      int(number_1)
      int(number_2)
    except:
      error_3 = "Error: Numbers must only contain digits."
      return error_3
    #Evaluate if number are short enough
    if len(number_1) > 4 or len(number_2) > 4:
      error_4 = "Error: Numbers cannot be more than four digits."
      return error_4
    #Arrange each string
    if len(number_1) > len(number_2):
      longer = len(number_1)
    else:
      longer = len(number_2)
    
    b_line_2 = longer + 2
    line_1 += "  " + (longer - len(number_1))*" " + number_1 + space
    line_2 += op_sign + (longer - len(number_2))*" " + number_2 + space
    line_3 += "-"*b_line_2+ space
    r = str(eval(problem))
    result += "  " + (longer - len(r))*" " + r + space

  #Decide if return problem solved or not
  if bool(arg) is True:
    print(bool(arg))
    arranged_solved = line_1[:-4] + "\n" + line_2[:-4] + "\n" + line_3[:-4] + "\n" + result[:-4]
    return arranged_solved
  else:
    print(bool(arg))
    arranged_problems = line_1[:-4] + "\n" + line_2[:-4] + "\n" + line_3[:-4]
    return arranged_problems

actual = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43"], False)

print(arithmetic_arranger(actual))
