import check50
import random

@check50.check()
def exists():
  check50.exists("main.py")

@check50.check()
def output_6_for_1_2_3():
  check50.run("python3 main.py").stdin("3").stdin("1").stdin("2").stdin("3").stdout("6")

@check50.check()
def output_10_for_1_2_3_4():
  check50.run("python3 main.py").stdin("4").stdin("1").stdin("2").stdin("3").stdin("4").stdout("10")

@check50.check()
def output_15_for_1_2_3_4_5():
  check50.run("python3 main.py").stdin("5").stdin("1").stdin("2").stdin("3").stdin("4").stdin("5").stdout("15")
