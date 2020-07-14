num = int(input("Enter the number - "))
temp = num
digit = 0
while temp > 0:
 r = temp % 10
 digit = (digit*10) + r
 temp //= 10
if num == digit:
  print (num,"is a palindrome number")
else:
  print (num,"is not a palindrome number")
