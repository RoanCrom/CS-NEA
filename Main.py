import random

def start () :

    question_list =["1","2","3","4","5"]
    answer_list = ["a","a","a","a","a"]

    
    x = random.randint([0,4])
    
    Question = question_list[x]
    Answer = answer_list[x]

    print(Question)
    print(Answer)


start()
