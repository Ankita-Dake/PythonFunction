# define function
def demo():
    print('hello world')


demo()


def show():
    print('this is function')


show()


# function parameter
def sample(name):
    print("my name is", name)


sample('ankita')


# 2 parameter in function
def sample1(name, age):
    print('my name is', name)
    print('my age is', age)


sample1('nikita', 20)


# default parameter value
def sample2(name, age=32, number=3878475):
    print('my name is', name)
    print('my age is', age)
    print('my number is', number)


sample2('om')


# passing a List as an argument
def showList(lang):
    for x in lang:
        print(x)


lang = ['HTML', 'CSS', 'Boostrap', 'Python']

showList(lang)


# another example
def List1(list1):
    list1.append(20)
    list1.append(30)
    print(list1)


list1 = [10, 50, 40, 60]

List1(list1)


# another example
def add(a, b):
    print('sum =', a + b)


a = int(input('enter a'))
b = int(input('enter b'))

add(a, b)

# Lambda function
i = lambda a: a + 5
print(i(5))

# examples
a = lambda i, j: i * j
print(a(2, 3))

z = lambda p, q, r: p * q * r
print(z(2, 3, 4))


