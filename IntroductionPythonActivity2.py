str result


def divis_by_seven_not_multiple_five(int1, int2):
    x = range(int1, int2)
    for n in x:
        if n %7 == 0 and n %5 != 0:
            result += str(i)+", "

int1 = int(input("Enter your first number!"))
int2 = int(input("Enter your second number!"))
print(divis_by_seven_not_multiple_five(int1, int2))