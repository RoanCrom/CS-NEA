import json
import random


def load_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


question_list = load_questions("Questions.json")

weight_list = [1] * len(question_list)

current_index = None
current_question = ""
current_answer = ""

correct = 0
questions_asked = 0

total_questions = 3


def new_question():
    global current_index
    global current_question
    global current_answer

    current_index = random.choices(
        range(len(question_list)),
        weights=weight_list
    )[0]

    current_question = question_list[current_index]["question"]
    current_answer = question_list[current_index]["answer"]

    return current_question


def check_answer(user_answer):
    global correct
    global questions_asked

    questions_asked += 1

    if user_answer.lower().strip() == str(current_answer).lower().strip():

        correct += 1

        if weight_list[current_index] > 1:
            weight_list[current_index] -= 1

        return True

    else:
        weight_list[current_index] += 1

        return False
