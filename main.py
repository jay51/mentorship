

def ask_user():
    num1 = int(input("First Number >: "))
    num2 = int(input("Second Number >: "))

    result = [num1, num2]
    return result

def write_operation(op, num1, num2, result):

  string = f"operation: {op} {num1}, {num2}\n"
  rs = f"result:  {result}\n"

  file.write(string)
  file.write(rs)
  file.flush()


file = open("./math", "w")

# operation = 'ADD'
# num1 = 4
# num2 = 4

# string = "opertion: " + operation + str(num1) + ", "  + str(num2) + "\n"
# file.write(string)
# file.write("result: 3\n")

# file.write("opertion: Sub 5, 4\n")
# file.write("result: 1\n")

while True:
  print("""
  1- Add numbers
  2- Sub numbers
  3- Mul numbers
  4- exit
  
  """)

  value = input(">: ")

  if value == "1":
    numbers = ask_user()
    result = numbers[0] + numbers[1]
    print("result >: ", result )

    # wite to file
    # > oporation: ADD 1, 2
    # > result: 4

    # string = "operation: ADD " +  str(numbers[0])  + ", "  + str(numbers[1]) + "\n"
    # rs = "result: " + str(result) + "\n"

    # string = f"operation: ADD  {numbers[0]}, {numbers[1]}\n"
    # rs = f"result:  {result}\n"

    # file.write(string)
    # file.write(rs)
    # file.flush()
    write_operation("ADD", numbers[0], numbers[1], result)


  if value == "2":
    numbers = ask_user()
    result = numbers[0] - numbers[1]
    print("result >: ", result )

    # wite to file
    # > oporation: Sub 2 2
    # > result: 0
    # string = f"operation: SUB {numbers[0]}, {numbers[1]} \n"
    # rs = f"result : {result}\n"

    # file.write(string)
    # file.write(rs)
    # file.flush()
    write_operation("SUB", numbers[0], numbers[1], result)

  if value == "3":
    numbers = ask_user()
    result = numbers[0] * numbers[1]
    print("result >: ", result )

    # wite to file
    # > oporation: Mul 2 2
    # > result: 4

    # string = f"Operation: Mul {numbers[0]} , {numbers[1]}\n"
    # rs = f"result: {result}\n"

    # file.write(string)
    # file.write(rs)
    # file.flush()
    write_operation("MUL", numbers[0], numbers[1], result)
 

  if value == "4":
    break
  dont forget to 