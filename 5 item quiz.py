# Python 5 multiplication Quiz

questions = ("What is 1x1 ?",
             "What is 2x2 ?",
             "What is 7x7 ?",
             "What is 4x4 ?",
             "What is 8x8 ?")

options = (("A. 1","B. 5","C. 6","D. 7"),
           ("A. 8","B. 4","C. 7","D. 2"),
           ("A. 49","B. 15","C. 9","D. 20"),
           ("A. 16","B. 10","C. 4","D. 80"),
           ("A. 64","B. 32","C. 18","D. 20"))

answers = ("A","B","A","A","A")
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