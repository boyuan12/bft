import check50
import random

def answer(grade):
  grade = int(grade)
  if grade > 100 or grade < 1:
    return "Invalid"
  else:
    if grade >= 90 and grade <= 100:
      return "A"
    elif grade >= 80 and grade <= 89:
      return "B"
    elif grade >= 70 and grade <= 79:
      return "C"
    elif grade >= 60 and grade <= 69:
      return "D"
    else:
      return "F"

@check50.check()
def exists():
  check50.exists("main.py")

@check50.check()
def output_A_for_100():
  check50.run("python3 main.py").stdin("100").stdout("A")

@check50.check()
def output_A_for_95():
  check50.run("python3 main.py").stdin("95").stdout("A")

@check50.check()
def output_A_for_90():
  check50.run("python3 main.py").stdin("90").stdout("A")

@check50.check()
def output_B_for_80():
  check50.run("python3 main.py").stdin("80").stdout("B")

@check50.check()
def output_C_for_79():
  check50.run("python3 main.py").stdin("79").stdout("C")

@check50.check()
def output_invalid_for_input_greater_than_100():
  check50.run("python3 main.py").stdin(str(random.randint(101, 500))).stdout("Invalid")

@check50.check()
def output_invalid_for_input_greater_than_100():
  check50.run("python3 main.py").stdin(str(random.randint(-100, 1))).stdout("Invalid")

@check50.check()
def random_check_1():
  num = random.randint(1, 101)
  check50.run("python3 main.py").stdin(str(num)).stdout(answer(num))

@check50.check()
def random_check_2():
  num = random.randint(1, 101)
  check50.run("python3 main.py").stdin(str(num)).stdout(answer(num))

@check50.check()
def random_check_3():
  num = random.randint(1, 101)
  check50.run("python3 main.py").stdin(str(num)).stdout(answer(num))
