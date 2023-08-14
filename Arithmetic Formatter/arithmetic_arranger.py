def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  # Initialize strings to store different lines of the arranged problems
  arranged_problems = ""
  first_line = ""
  second_line = ""
  dashes_line = ""
  answers_line = ""

  # Iterate through each arithmetic problem in the list
  for problem in problems:
    operands = problem.split()  
    operator = operands[1]
    num1 = operands[0]
    num2 = operands[2]

    
    if operator != '+' and operator != '-':
      return "Error: Operator must be '+' or '-'."

    
    if not num1.isdigit() or not num2.isdigit():
      return "Error: Numbers must only contain digits."

    
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."

   
    if operator == '+':
      answer = str(int(num1) + int(num2))
    else:
      answer = str(int(num1) - int(num2))

    
    width = max(len(num1), len(num2)) + 2

    # Build the different lines for the arranged problem
    first_line += num1.rjust(width) + '    '
    second_line += operator + num2.rjust(width - 1) + '    '
    dashes_line += '-' * width + '    '

    
    if show_answers:
      answers_line += answer.rjust(width) + '    '

  
  arranged_problems += first_line.rstrip() + '\n'
  arranged_problems += second_line.rstrip() + '\n'
  arranged_problems += dashes_line.rstrip()
  if show_answers:
    arranged_problems += '\n' + answers_line.rstrip()

  return arranged_problems

# Test cases
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
