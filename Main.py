import json
import random

def load_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def start():
    q_path = "Questions.json" 
    question_list = load_questions(q_path)
    
    weight_list = [1] * len(question_list)
    totalQ = 3  

    while True:
        cor = 0
        chosen_questions = []
        chosen_answers = []
        chosen_indices = []

        for _ in range(totalQ):
            idx = random.choices(range(len(question_list)), weights=weight_list)[0]
            
            chosen_questions.append(question_list[idx]["question"])
            chosen_answers.append(question_list[idx]["answer"])
            chosen_indices.append(idx)

        for o in range(len(chosen_questions)):
            user_ans = input(f"\n{chosen_questions[o]}\nYour answer: ")
            current_idx = chosen_indices[o]

            if user_ans.lower().strip() == str(chosen_answers[o]).lower().strip():
                print("Correct!")
                cor += 1
                if weight_list[current_idx] > 1:
                    weight_list[current_idx] -= 1
            else:
                print(f"Incorrect. The correct answer was: {chosen_answers[o]}")
                weight_list[current_idx] += 1

        print(weight_list)
        print(f"You got {cor} out of {totalQ} correct!")


start()
