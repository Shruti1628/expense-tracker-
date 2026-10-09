expenses=[]# Expense in dictionary for
print("Welcome To Track Your Expense:💰")
while True:
    print("===Menu===")
    print("1.ADD YOUR EXPENSE :")
    print("2.VIEW ALL THE EXPENSE:")
    print("3.VIEW THE TOTAL EXPENSE:")
    print("4.EXIT")
    choice=int(input("Enter Your Choice:"))

    #ADD Expence
    if choice ==1:
        date = input("Enter the date When You Spent Money:")
        category =input("Enter the Category On What You Spend eg(book,dress,makeup,phone,etc)")
        description=input("Give a short description:")
        amount =int(input("enter the amount you spend:"))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expenses.append(expense)
        print("Done.Your Expense Is Successfully Add:💵")

        #view the all the expense
    elif choice==2:
       if(len(expenses)==0):
        print("You Have Not Add Any Expense In your Expense List:")
       else:
        print("=== Your Expense List Is:")  
        count=1  
        for eachexpense in expenses:
           print(f"Number of Expense{count}-{eachexpense["date"]},{eachexpense["category"]},{eachexpense["description"]},{eachexpense["amount"]}")
           count+=count

        #View the Total expense 
    elif choice==3:
       total=0
       for eachexpense in expenses:
          total = total + eachexpense["amount"] 
       print(f"\n Your Total Expense Spended is : {total} 💰")    

         # Exist
    elif choice==4:
      print("Thankyou For  Using Are Expense Tracking System:")
      break
    else:
       print("Invalid Choice:⚠️")
             

   

