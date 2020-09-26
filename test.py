print("Todolist")


def checktasks():
    with open('todolistnew.txt', 'r+') as todolist:
        print('Please enter check your tasks: ', todolist.name)
        tasks = todolist.read()
        print(tasks)


def check1():
    if check_input == '1':
        checktasks()
        print('Thank you')


def check2():
    if check_input == '2':
        task_input = '0'
        while task_input != '':
            task_input = input(
                'Please input your tasks. When entering the number 0 will be saved.: ')
            with open('todolistnew.txt', 'a+') as todolist:
                todolist.write('* ' + task_input + '\n')
            if task_input == '':
                lines = open('todolistnew.txt').readlines()
                open('todolistnew.txt', 'w').writelines(lines[:-1])
                checktasks()
                break
            elif task_input == '0':
                exit(0)
                print('Thank you')


def check3():
    if check_input == '3':
        checktasks()
        while True:
            delete_input = int(
                input('Which task line do you want to delete? '))
            with open('todolistnew.txt', 'r') as todolist:
                lines = todolist.readlines()
            with open('todolistnew.txt', 'w') as todolist:
                todolist.writelines(
                    lines[:delete_input - 1] + lines[delete_input:])
            checktasks()
            print('Thank you')
            break


def check4():
    if check_input == '4':
        print('Thank you')


print('This is a simple to do list program.')
print('What do you want to do?')
print('1 - Check your tasks')
print('2 - Add your tasks')
print('3 - Delete your tasks')
print('4 - End this program')

check_input = input('Please select 1 , 2 , 3 , 4 : ')
check1()
check2()
check3()
check4()

print("\n__________________________________________________________________________________________________________\n")

print("1.")


def FizzBuZZZ():
    num = 1
    counter = 1
    while (num <= 100):
        if counter % 20 == 1:
            print('')
        if num % 15 == 0:
            print('FizzBuzz', end=' ')
        elif num % 3 == 0:
            print('Fizz', end=' ')
        elif num % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(num, end=' ')
        num += 1
        counter += 1


FizzBuZZZ()

print("\n__________________________________________________________________________________________________________\n")

print("2.")

year = int(input('Input year: '))
if year % 400 == 0:
    print(year, '-> true')
elif year % 400 != 0 and year % 100 != 0 and year % 4 == 0:
    print(year, '-> true')
else:
    print(year, '-> false')
print("\n__________________________________________________________________________________________________________\n")

print("3.1")


def NumRight():
    n = int(input("Input number (n):"))
    for i in range(n):
        print('*' * (i+1))


NumRight()

print("\n__________________________________________________________________________________________________________\n")

print("3.2")


def Switch():
    n = int(input("Input number (n):"))
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("")


Switch()

print("\n__________________________________________________________________________________________________________\n")

print("3.3")


def triangle():
    n = int(input("Input number (n):"))
    for row in range(1, n+1):
        for col in range(1, 2*n):
            if row+col == n+1 or col-row == n-1:
                print("*", end=" ")
            else:
                print(end=" ")
        print()


triangle()
print("\n__________________________________________________________________________________________________________\n")
print("3.4")


def pattern():
    num = int(input("Please enter Number : "))
    for i in range(num):
        print("".join("*"
                      if j == i or num - 1 - j == i
                      else " "
                      for j in range(num)))


pattern()

print("\n__________________________________________________________________________________________________________\n")

print("3.5")


def diamond():
    n = int(input("Input number diamond's height: "))
    for i in range(1, n, 2):
        print(" "*(n//2-i//2), "*"*i)
    for i in range(n, 0, -2):
        print(" "*(n//2-i//2), "*"*i)


diamond()
print("\n__________________________________________________________________________________________________________\n")

print("3.6 ")


def ABCDE():
    number = int(input('Input number (n): '))
    column = number * 2 - 1
    center = number - 1

    for i in range(0, center + 1):
        for j in range(0, column):
            if j == center - i or j == center + i:
                print(end='+')
            elif i + j <= center - 1:
                print(end='A')
            elif j - i > center:
                print(end='B')
            else:
                print(end='E')
        print()

    for i in range(center - 1, -1, -1):
        for j in range(0, column):
            if j == center - i or j == center + i:
                print(end='+')
            elif j < center - i:
                print(end='C')
            elif j > center + i:
                print(end='D')
            else:
                print(end='E')
        print()


ABCDE()

print("\n__________________________________________________________________________________________________________\n")

print("Medium : ")


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def printPrime(n):
    for i in range(2, n + 1):
        if isPrime(i):
            print(i, end=" ")


if __name__ == "__main__":
    n = int(input("Enter number: "))
    printPrime(n)
