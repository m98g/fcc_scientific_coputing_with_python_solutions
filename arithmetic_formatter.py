def arithmetic_arranger(problems, flag = False):
  if len(problems) > 5:
    return("Error: Too many problems.")
  first_line = []
  second_line = []
  third_line = []
  fourth_line = []
  allowed_operations = ("+", "-")
  
  for i in range(len(problems)):
    parts = [x for x in problems[i].split(" ")]
    if parts[1] not in allowed_operations:
      return("Error: Operator must be '+' or '-'.")

    if  len(parts[0]) > 4 or len(parts[2])  > 4:
      return("Error: Numbers cannot be more than four digits.")

    if parts[0].isdigit() != True or parts[2].isdigit() != True:
      return('Error: Numbers must only contain digits.')
      
    length = max(len(y) for y in parts) + 2

    first_line.append((" " * (length - len(parts[0])) + parts[0]))
    second_line.append(parts[1] + " " * (length - len(parts[2]) - 1) + parts[2])
    third_line.append("-" * length)

    if i != len(problems) - 1:
      first_line.append(" " * 4)
      second_line.append(" " * 4)
      third_line.append(" " * 4)

    if flag:
      result = eval(problems[i])
      fourth_line.append(" " * (length - len(str(result))) + str(result))
      if i != len(problems) - 1:
        fourth_line.append(" " * 4)



  if flag:
    all = ["".join(first_line), "".join(second_line), "".join(third_line), "".join(fourth_line)]
    return("\n".join(all))
  else:
    all = ["".join(first_line), "".join(second_line), "".join(third_line)]
    return("\n".join(all))


print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))