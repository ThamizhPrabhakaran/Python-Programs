def equalNumbers(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False
print(equalNumbers([1,2,3,4]))
print(equalNumbers([2,2,3,4,5]))
