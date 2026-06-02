try:
    num = 8
    print("The number exception is",num)
except ValueError as ex:
    print("Exception")

#Activity2
try:
    num_1 = 3
    num_2 = 7
    result = num_1/num_2
except ZeroDivisionError:
    print("Division by 0 is error")
except SyntaxError:
    print("error_1")
except:
    print("error_2")
else:
    print("No exception")
finally:
    print("This will excute no matter what")

#Activity3
valid = False
while not valid:
    try:
        n = 16
        while n % 2 == 0:
            print("Bye")
        valid is True
    except ValueError:
        print("Invalid")