from math import factorial


def fib_fn(input):
  try:
    if input <= 1:
      return input
    else:
      return(fib_fn(input-1) + fib_fn(input-2))
  except TypeError:
    return


def factorial_fn(input):

  return factorial(input)
