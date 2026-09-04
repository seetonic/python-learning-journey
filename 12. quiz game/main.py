questions = ("Q01. What is the only mammal that can truly fly?",
             "Q02. Which planet in our solar system is known as the Red Planet?",
             "Q03. How many colors are there in a rainbow?",
             "Q04. What is the largest ocean on Earth?",
             "Q05. Which gas do plants absorb from the air to make their own food?")

options = (("A.Flying squirrel", "B. Bat", "C. Flying lemur", "D. Eagle"),
           ("A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"),
           ("A. 5", "B. 6", "C. 7", "D. 8"),
           ("A. Atlantic Ocean", "B.  Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"),
           ("A. Oxygen", "B. Carbon dioxide", "C. Nitrogen", "D. Hydrogen"))

answers = ("B", "C", "C", "D", "B")
guesses = []
Qus_num = 0
score = 0

for question in questions:
    print("----------------------------------------------")
    print(question)
    for option in options[Qus_num]:
        print(option)

    guess = input("your answer (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[Qus_num]:
        score += 1
        print("answer is correct.")
    else:
        print(f"incorrect! correct answer is: {answers[Qus_num]} ")
    Qus_num += 1

print("----------------------------------------")

print("Answers: ", end=" ")

for answer in answers:
    print(answer, end=" ")

print()
print("Guesses: ", end=" ")

for guess in guesses:
    print(guess, end=" ")

print()
total = int(score/len(questions)*100)
print(f"your total score is: {total}%")