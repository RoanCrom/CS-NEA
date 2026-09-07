import random

question_list =["1","2","3","4","5"]
answer_list = ["a","b","c","d","e"]
weight_list = [1,1,1,1,1]

def start () :
    
    cor = 0
    totalQ = 10
    
    Question =[]
    Answer =[]
    QuestionIndex=[]

    for i in range (0,totalQ):
            
        x = random.choices(range(len(question_list)),weights=weight_list)[0]
        
        Question.append(question_list[x])
        Answer.append(answer_list[x])
        QuestionIndex.append(x)

        

    for o in range (0, len(Question)) :
        

        AskedQ = input(f"{Question[o]}\n")

        CurrentIndex = QuestionIndex[o]

        if AskedQ.lower() == Answer[o] :
            print("Correct")

            cor += 1

            if weight_list[CurrentIndex] > 1:
                weight_list[CurrentIndex] -= 1
            else:
                weight_list[CurrentIndex] = weight_list[CurrentIndex]
        else:
            print("incorrect")
            weight_list[CurrentIndex] += 1


    print(weight_list)
    print(f"you got {cor} out of {totalQ}")

    start()
    
start()
