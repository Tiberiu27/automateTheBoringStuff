
def collaz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1



print("say a number")
x = input()

while x != 1:
    try:
        x = collaz(int(x))
    except ValueError:
        print("that's not a number")
        break