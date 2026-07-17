import time

print("""Welcome to KBC
Rules:
1. Each correct answer gives Rs.100
2. All correct answers → Rs.2000
""")
print(f"We will Redirect in 3 Seconds\nBest Luck\n")
time.sleep(3)

questions = [
    ["Q1 What is the capital of India?",
     "Kolkata", "Chennai", "New Delhi", "Mumbai", 3],

    ["Q2 Which planet is known as the Red Planet?",
     "Mars", "Venus", "Earth", "Jupiter", 1],

    ["Q3 Who is known as the Father of Indian Navy?",
     "Chatrapati Shivaji Maharaj", "Bhagat Singh", "Subhash Chandra Bose", "Maharana Rajput", 1],

    ["Q4 How many days are there in a week?",
     "8", "7", "6", "5", 2],

    ["Q5 Which animal is known as the King of the Jungle?",
     "Elephant", "Tiger", "Leopard", "Lion", 4],

    ["Q6 What is 5 + 3?",
     "7", "9", "6", "8", 4],

    ["Q7 Which color is in the Indian national flag?",
     "Brown", "Green", "Pink", "Black", 2],

    ["Q8 Which festival is called the Festival of Lights?",
     "Christmas", "Eid", "Diwali", "Holi", 3],

    ["Q9 Which gas do plants absorb?",
     "Hydrogen", "Carbon Dioxide", "Oxygen", "Nitrogen", 2],

    ["Q10 How many continents are there?",
     "6", "8", "5", "7", 4]
]
score = 0

for q in questions:
    print(q[0])
    print(f"1. {q[1]}")
    print(f"2. {q[2]}")
    print(f"3. {q[3]}")
    print(f"4. {q[4]}")

    ans = int(input("Enter the option no: "))
    if ans == q[5]:
        print("Correct Answer\n")
        score +=1
    else:
        print("Incorrect Answer\n")
        break
  
if score == 10:
      print(f"Your correct answer are {score} and you win Rs.:{(score * 100)} And bonus Money 1000\nTotal Rs.2000")
elif score > 0:
    print(f"Your correct answer are {score} and you win Rs.:{score * 100}")
else :
    print("You lost!!!")