questions = [
    {"Prompt" : "What comic did Byeonduck made?" , 
     "Options" : ["A. Painter of the night", "B. Semantic Errors", "C. Smyran & Capri"],
     "Answer" : "A"} ,
    
    {"Prompt" : "Who is the eldest son of the Yoon family?" , 
     "Options" : ["A. Yoon Seungho", "B. Jaeyoung Jang", "C. Lee Jihwa"],
     "Answer" : "A"} ,
    
    {"Prompt" : "Who is the Painter from POTN?" , 
     "Options" : ["A. Lee Jihwa", "B. Ryu Chihye", "C. Baek-Nakyum"],
     "Answer" : "C"} ,
    
    {"Prompt" : "What was the name of \"No Name Assassin\"?" , 
     "Options" : ["A. In-Hun", "B. Young Seung-won", "C. Meumyeong"],
     "Answer" : "C"} ,
    
    ]

def quiz(questions):
    score = 0
    for question in questions:
        print(question["Prompt"])
        for option in question["Options"]:  
            print(option)
        answer = input("Enter your option : ")
        if answer == question["Answer"]:
            score = score+1
            print("Correct answer")
        else:
            print("Incorrect answer")
    
    print(f"Your score is {score} out of {len(questions)}.")
    return score

quiz(questions)