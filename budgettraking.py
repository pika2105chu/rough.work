

print("Hello, lets see todays budget and your expenses")
budget = float(input("Enter your todays budget : Rs."))

expense = []

def budgettracker():
    
    while True:
        print("\n1. Add your expenses one by one : \n2. Show the amount left in the budget : \n3. Exit the program\n")
        choice = int(input("Enter your choice from 1,2,3 : "))
        
        if choice==1:
            a= float(input("\nEnter your expense : Rs."))
            b = input("enter your expense description : ")
            expense.append(a)
            
        elif choice == 2:
            z=budget
            for i in expense:
                z=z-i
            print(f"Amount left in the budget is Rs.{z}")
            sum=0
            for i in expense:
                sum=sum+i
            print(f"so the sum of total expenses is Rs.{sum}")
            
        elif choice == 3:
            print("Exitting and going to bed nowww\n")
            break
            
        else:
            print("you entered the wrong choice")

budgettracker()