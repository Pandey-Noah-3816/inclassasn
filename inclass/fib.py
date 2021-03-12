
def fib_fn(input):
  try:
    if input <= 1:
      return input
    else:
      return(fib_fn(input-1) + fib_fn(input-2))
  except TypeError:
    return


def factorial_fn(input):
  if input < 0:
    return("bad")
  if input == 0:
    return 1
  x =1
  for i in range(1,input + 1):
    x = x*i

  return x

