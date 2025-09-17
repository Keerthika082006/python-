#quiz game

questions=("How many bones are in the human body?:",
           "which animal lays the largest egg?:",
           "how many elements are in the periodic table?:")

options=(("A.206","B.208","C.209",),
         ("A.whale","B.ostrich","C.elephant",),
         ("A.119","B.118","C.117",))

answers=("A","B","B")
guesses=[]
score=0
question_num=0

for question in questions:
    print("---------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess=input("enter(A,B,C):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("correct")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1
    
print("--------------------------------")
print("           RESULTS              ")
print("--------------------------------")

print("answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("guess: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score=int(score/len(questions)*60)
print(f"your score is :{score}%")

if score==60:
    print("execlent!")
elif score>=40:
    print("average!")
else:
    print("poor!")



    
