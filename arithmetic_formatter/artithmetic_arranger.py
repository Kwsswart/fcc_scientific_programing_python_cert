def arithmetic_arranger(problems, display=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_row = ''
    second_row = ''
    dash_row = ''
    answer_row = ''

    for prob in problems:
      if "/" in prob or "*" in prob:
        return "Error: Operator must be '+' or '-'."

      if not prob.split()[0].isdigit() or not prob.split()[-1].isdigit():
          return "Error: Numbers must only contain digits."

      if len(prob.split()[0]) > 4 or len(prob.split()[-1]) > 4:
          return "Error: Numbers cannot be more than four digits."

      first_n = prob.split()[0]
      operator = prob.split()[1]
      second_n = prob.split()[-1]
      longest = first_n
      other = second_n
      changed = False

      if len(longest) < len(second_n):
          longest = second_n
          other = first_n
          changed = True

      if changed:
          longest = operator + ' ' + longest
          spaces = ''
          for i in range(len(longest) - len(other)):
              spaces += ' '
          other = spaces + other
      else:
          longest = '  ' + longest
          spaces = ''
          for i in range(len(longest) - len(other) - 1):
              spaces += ' '
          other = spaces + other
          other = operator + other

      dashes = ''

      for i in range(len(longest)):
          dashes = "-" + dashes

      if changed:
          first_row = first_row + other + "    "
          second_row = second_row + longest + "    "
      else:
          first_row = first_row + longest + "    "
          second_row = second_row + other + "    "

      dash_row = dash_row + dashes + "    "

      if operator == "+":
          answer = str(int(first_n) + int(second_n))
          spaces = ''
          for i in range(len(longest) - len(answer)):
              spaces = spaces + ' '
          answer = spaces + answer
      else:
          answer = str(int(first_n) - int(second_n))
          spaces = ''
          for i in range(len(longest) - len(answer)):
              spaces = spaces + ' '
          answer = spaces + answer
      answer_row = answer_row + answer + "    "
        
    spaces_required = ''
    first_row = first_row.strip()
    second_row = second_row.strip()

    for i in range(len(second_row) - len(first_row)):
      spaces_required += ' '

    answer_spaces_required = ' '
    answer_row.strip()
    second_row = second_row.strip()

    for i in range(len(second_row) - len(answer_row)):
      answer_spaces_required += ' '

    if display == True:
        arranged_problems = spaces_required + first_row.strip() + "\n" + second_row.strip() + "\n" + dash_row.strip() + "\n" + answer_spaces_required + answer_row.strip()
    else:
        arranged_problems = spaces_required + first_row.strip() + "\n" + second_row.strip() + "\n" + dash_row.strip()

    return arranged_problems