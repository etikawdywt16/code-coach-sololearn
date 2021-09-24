import math

houses = int(input())

if houses >= 3:
  prob = 2 / houses * 100
  print(math.ceil(prob))
