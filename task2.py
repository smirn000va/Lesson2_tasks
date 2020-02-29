a='python'
b='learn'

def func(a,b):
   if isinstance(a, str) and isinstance(b, str):
      return 0

def func_1(a,b):   
   if a.lower() == b.lower():
      return 1

def func_2(a,b):   
   if a.lower() != b.lower() and len(a)>len(b):
      return 2

def func_3(a,b):   
   if a.lower() != b.lower() and b=='learn':
      return 3

print(func(a, b))
print(func_1(a, b))
print(func_2(a, b))
print(func_3(a, b))
      
          
    

