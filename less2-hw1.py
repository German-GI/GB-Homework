int = 5
float = 1.2
str = "Hello world"
list = ['a', '2']
tuple = ('b', '3')
dict = {'city': 'Moscow', 'country': 'Russia'}
list = [int, float, str, list, tuple, dict]
for i in list:
    print(f'{i} is {type(i)}')
