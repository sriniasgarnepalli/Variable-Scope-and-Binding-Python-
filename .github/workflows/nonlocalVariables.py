def counter():
  num = 0
  def incrementer():
    num += 1
    return num
  return incrementer

a = counter()
a()

# The above code will give the error "If you try running this code, you will receive an UnboundLocalError because the num variable is referenced before
it is assigned in the innermost function."

