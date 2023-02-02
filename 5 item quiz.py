# Python 5 item genshin/random Quiz

questions = ("Who is the 77th Director of the Wangsheng Funeral Parlor ?",
             "What is the name of dendro archon ?",
             "What is most broken elemental reaction in genshin impact ?",
             "What is the 4th planet in our solar system ?",
             "What is 8x8 ?")

options = (("A. Hu tao","B. Qiqi","C. Ganyu","D. Zhongli"),
           ("A. Nahida","B. Raiden","C. Venti","D. Zhongli"),
           ("A. melt","B. swril","C. Vaporized","D. Hyperbloom"),
           ("A. Jupiter","B. Earth","C. Mars","D. Uranus"),
           ("A. 64","B. 32","C. 18","D. 20"))

answers = ("A","A","C","C","A")
guesses = []
score = 0
question_num = 0

for questions in questions:
    print("---------------------")
    print(questions)
    for everyoption in options[question_num]:
        print(everyoption)

    guess = input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer ")
    question_num += 1

print("---------------------")
print("          RESULTS            ")
print("---------------------")

print("answers:",end="")

for key in answers:
    print(key,end=" ")
print()

print("guesses:",end="")

for guess in guesses:
    print(guess,end=" ")
print()

score = int(score / len(questions) * 80)
print(f"Your score is: {score}%")