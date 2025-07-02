import random
from termcolor import cprint

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'

def ask_question(index, question, options):
    print(f'Question {index}: {question}')
    for option in options:
        print(option)

    return input('Your answer: ').upper().strip()


def run_quiz(quiz):
    random.shuffle(quiz)

    score = 0

    for index, item in enumerate(quiz, 1):
        answer = ask_question(index, item[QUESTION], item[OPTIONS])

        if answer == item[ANSWER]:
            cprint('Correct!', 'green')
            score += 1
        else:
            cprint(f'Incorrect! The correct answer is {item[ANSWER]}', 'red')

        print()

    print(f"Quiz is over! Your score is {score} out of {len(quiz)}.")


def main():
    quiz = [
        {
            QUESTION: 'What is the Capital of India',
            OPTIONS: ['A.Delhi', 'B.Mumbai', 'C.New Delhi', 'D.New Mumbai'],
            ANSWER: 'C'
        },
        {
            QUESTION: 'What is the national bird of India',
            OPTIONS: ['A.Eagle', 'B.Peacock', 'C.Dove', 'D.Swan'],
            ANSWER: 'B'
        },
        {
            QUESTION: 'What is the national animal of India',
            OPTIONS: ['A.Tiger', 'B.Lion', 'C.Leopard', 'D.Jaguar'],
            ANSWER: 'A'
        }
    ]
    run_quiz(quiz)

if __name__ == '__main__':
    main()