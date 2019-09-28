def fizzbuzz(n):
  a = []
  A = 0
  for i in range(n):
    if i%3==0 or i%5==0:
      a.append(i)
  for j in range(len(a)):
    A=A+a[j]
  return(A)
print(fizzbuzz(41))
print(fizzbuzz(1001))
