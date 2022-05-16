import random
import sys

def main():
    level = get_level()
    correct_answers = 0
    wrong_answer = 0
    for _ in range(10):
        num1, num2 = generate_integer(level)
        user_solution = get_user_solution(num1, num2)
        solution = num1 + num2
        if user_solution == solution:
            correct_answers += 1
        else:
            while wrong_answer < 2:
                print("EEE")
                wrong_answer += 1
                user_solution = get_user_solution(num1, num2)
                if user_solution == solution:
                    print(wrong_answer)
                    wrong_answer = 0
                    break
            if wrong_answer >= 2:
                print(f"{num1} + {num2} = {solution}")
                wrong_answer = 0

    print("Score:", correct_answers)
    sys.exit()


def get_user_solution(n1, n2):
    try:
        user_solution = int(input(f"{n1} + {n2} = "))
        return user_solution
    except ValueError:
        get_user_solution(n1, n2)


def get_level():
    try:
        level = int(input("Level: "))
        if level < 1 or level > 3:
            raise ValueError
        else:
            return level
    except ValueError:
        get_level()


def generate_integer(level):
    if level == 1:
        num1 = random.randrange(0, 10)
        num2 = random.randrange(0, 10)
    elif level == 2:
        num1 = random.randrange(10, 100)
        num2 = random.randrange(10, 100)
    else:
        num1 = random.randrange(100, 1000)
        num2 = random.randrange(100, 1000)
    return num1, num2


if __name__ == "__main__":
    main()