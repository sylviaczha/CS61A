"""1.1"""
def multiply(m,n):
  if m == 1:
    return n
  else:
    return n + multiply(m-1, n)
  
 
print(multiply(45, 30)）
 
"""1.3"""
def hailstone(n):
  print (n)
  if n == 1:
       return 1
  elif n % 2 == 0:
       return 1 + hailstone (n // 2)
  else:
       return 1 + hailstone (n * 3 + 1)

a = hailstone(10)
print(a)
       
"""1.4"""
def merge(n1, n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10

print(merge(21, 31))

"""1.5"""
def make_func_repeater(f, x):
    def repeat(i):
        if i == 0:
            return x
        else:
            return f(repeat(i-1))
    return repeat
			
#OR
def make_func_repeater(f, x):
    def repeat(n):
        if n == 1:
            return f(x)
        else:
            return make_func_repeater(f, f(x))(n-1)
    return repeat

a = make_func_repeater(lambda x: x*5, 1)
print(a(2))

"""1.6"""
def is_prime(n):
    def prime_helper(k):
        if n == k:
            return True
        elif n == 1 or n % k == 0:
            return False
        else:
            return prime_helper(k+1)
    return prime_helper(2)

print(is_prime(10)) 
