import random
import sys

def main():
    level = get_level()
    operator = get_operator()
    print("Score:", check_solution(level, operator))
    sys.exit()


def check_solution(level, operator):
    correct_answers = 0
    wrong_answer = 0
    for _ in range(10):
        num1, num2 = generate_integer(level)
        user_solution = get_user_solution(num1, num2, operator)

        if operator == "+":
            solution = num1 + num2
        elif operator == "-":
            solution = num1 - num2
        elif operator == "*":
            solution = num1 * num2
        elif operator == "/":
            solution = num1 // num2
        
        if user_solution == solution:
            correct_answers += 1
        else:
            while wrong_answer < 2:
                print("EEE")
                wrong_answer += 1
                user_solution = get_user_solution(num1, num2, operator)
                if user_solution == solution:
                    print(wrong_answer)
                    wrong_answer = 0
                    break
            if wrong_answer >= 2:
                print(f"{num1} {operator} {num2} = {solution}")
                wrong_answer = 0
    return correct_answers


def get_user_solution(n1, n2, operator):
    try:
        user_solution = int(input(f"{n1} {operator} {n2} = "))
        return user_solution
    except ValueError:
        get_user_solution(n1, n2, operator)


def get_operator():
    try:
        operator = input("Enter a operant (+,-,*,/): ")
        if operator == "/":
            print("You don't have to care about decimal places!")
        if operator not in ["+", "-", "*", "/"]:
            raise ValueError
        else:
            return operator
    except ValueError:
        get_operator()


def get_level():
    try:
        level = int(input("Enter a level between 1 and 3: "))
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
