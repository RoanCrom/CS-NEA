import random

def start () :

    question_list =["1","2","3","4","5"]
    answer_list = ["a","b","c","d","e"]
    weight_list = [1,1,1,1,1,]


    while True:
            
        x = random.choices(range(len(question_list)),weights=weight_list)[0]
        
        Question = question_list[x]
        Answer = answer_list[x]

        AskedQ = input(f"{Question}\n")

        if AskedQ.lower() == Answer :
            print("Correct")

            if weights[x] > 1:
                weights[x] -= 1
            else:
                weights[x] = weights[x]
        else:
            print("incorrect")
            weights[x] += 1

start()
