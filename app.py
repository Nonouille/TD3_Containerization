import random
from fuzzywuzzy import fuzz


class Quiz:
    def __init__(self,mcq):
        self.mcq = MCQ_Question

    def askMcq(self):
        i = 1
        print(self.mcq["question"])
        for possibilitie in self.mcq["possibilities"] : 
            print(f"{i} : {possibilitie}")
            i+=1
        answer = int(input("What's your answer ? (use the numbers) : "))
        if answer == self.mcq["answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is :", self.mcq["possibilities"][self.mcq["answer"]-1])

MCQ_Question = {
    "question" : "What's the impostor among the new 7 Wonders of the World ?",
    "possibilities" : ["Great Wall of China","Alexandria Lighthouse","The Machu Pichu"],
    "answer" : 2
} 

history_quiz = Quiz(MCQ_Question)
history_quiz.askMcq()