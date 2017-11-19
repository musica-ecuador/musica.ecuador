from fuzzywuzzy import fuzz

result = fuzz.ratio("this is a test", "this is a test!")

print(result)


result =  fuzz.token_sort_ratio("this is a test", "this is a test!")

print(result)



result = fuzz.ratio('2h Para Todos', 'De La Gente & A2H I 2H Para Todos')

print(result)

result =  fuzz.token_sort_ratio('2h Para Todos', 'De La Gente & A2H I 2H Para Todos')

print(result)

str1 = 'Es Por Esto'
str2 = 'A2H & 420 THZ I Es Por Esto'
result = fuzz.ratio(str1,str2)

print(result)

 
result = fuzz.token_sort_ratio(str1,str2)

print(result)


name = "A2h+"

   

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = list(filter(lambda x: x % 2, fib))
print (result)