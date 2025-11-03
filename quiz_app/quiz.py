print("Welcome to the BBC Python Quiz!")

print("You will be asked 5 questions. Let's see how many you get right!\n")



score = 0



# Question 1

answer = input("1. What does 'BBC' stand for? ").strip().lower()

if answer == "british broadcasting corporation":

    print("✅ Correct!\n")

    score += 1

else:

    print("❌ Wrong. The correct answer is British Broadcasting Corporation.\n")



# Question 2

answer = input("2. What programming language is this quiz written in? ").strip().lower()

if answer == "python":

    print("✅ Correct!\n")

    score += 1

else:

    print("❌ Wrong. The correct answer is Python.\n")



# Question 3

answer = input("3. What symbol is used to start a comment in Python? ").strip()

if answer == "#":

    print("✅ Correct!\n")

    score += 1

else:

    print("❌ Wrong. The correct answer is #.\n")



# Question 4

answer = input("4. What function do we use to get user input in Python? ").strip().lower()

if answer == "input":

    print("✅ Correct!\n")

    score += 1

else:

    print("❌ Wrong. The correct answer is input().\n")



# Question 5

answer = input("5. What function is used to display text in Python? ").strip().lower()

if answer == "print":

    print("✅ Correct!\n")

    score += 1

else:

    print("❌ Wrong. The correct answer is print().\n")



print(f"You got {score}/5 correct!")

