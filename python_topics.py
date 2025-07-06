#syntax for list comprehension
#[expression for item in iterable if condition]
list_ex = [1, 2, 3, 4, 5]
list_comprehension = [val**2 for val in list_ex if val%2==0]
nested_list_comprehension = [x*y for x in range(3) for y in range(5)]


#syntax for dictionary comprehension
#[expression for item in iterable if condition]
key = [1, 2, 3, 4, 5]
values = ['a', 'b', 'c', 'd', 'e']
dict_comprehension = {k:v for k in key for v in values}
dict_comprehension_2 = {k:v for k,v in zip(key, values)}
nested_dict_comprehension = {
    v: {k: str(k)+v for k in key} for v in values
}

#lambda function
#syntax for lambda funciton - 
#lambda arguments : expression
calculate = lambda num: num**2 if num%2==0 else num**3
print(calculate(2))
#differences between normal function and lambda function
#NORMAL FUNCITON - DEFINED USING def keyword, definition of function can contain any number of lines. contains return statement
#LAMBDA FUNCTION - only one line of statement in definition - any number of arguments
#lambda is used inside sort, filter, map
sorted(key, lambda x: int(x))

#filter function - filters each element in sequence with the help of function whether its satisfying the condition defined in the function
#syntax for filter function - filter(function, sequence)
def even(n):
  return n%2==0
b = list(filter(even, key))
#we can use lambda fucntion to filter
b = list(filter(lambda num: num%2==0, key))

#reduce function -  # this returns the integer. it applies to all the elements sequentially.
#syntax for reduce function - reduce(function, sequence)
def even(n1, n2):
  return n1/2
b = reduce(even, key)
print(b) #- output 15
#we can use lambda fucntion to reduce
b = reduce(lambda num1, num2: num1+num2 , key)

#map function - used to apply particular function to each element in the sequence. it returns an iterable
#syntax for reduce function - reduce(function, sequence)
def even(n1):
  return n1/2
b = map(even, key)
print(list(b)) #- output 15
#we can use lambda fucntion to reduce
b = list(map(lambda num1: num1/2 , key))

#OBJECT ORIENTED PROGRAMMING


 





