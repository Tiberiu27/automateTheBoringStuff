#dumbMultiplicationQuiz
import time, random



score = 0
timelimit = time.time() + 8 #does not work

for question in range(10):
    tries = 0
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    print('What is %s times %s?' % (num1, num2))
    while tries < 3:
        answer = input()
        if answer == str(num1 * num2):
            score += 1
            print('Correct')
            time.sleep(1)
            break
        else:
            tries += 1
            print('guess again')


print(score)