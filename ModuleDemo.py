import UDF

while True:
    print("*"*50)
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Pattern")
    print("7. Exit")
    print("*"*50)
    choice=int(input("Enter Your Choice : "))

    if choice==1:
        n1=int(input("Enter Number : "))
        UDF.oddeven(n1)
        print("*"*50)
    elif choice==2:
        n1=int(input("Enter Number : "))
        n2=int(input("Enter Number : "))
        UDF.maxoftwo(n1,n2)
        print("*"*50)
    elif choice==3:
        n1=int(input("Enter Number : "))
        n2=int(input("Enter Number : "))
        n3=int(input("Enter Number : "))
        UDF.maxofthree(n1,n2,n3)
        print("*"*50)
    elif choice==4:
        n1=int(input("Enter Number : "))
        UDF.fibonacci(n1)
        print("*"*50)
    elif choice==5:
        n1=int(input("Enter Number : "))
        UDF.prime(n1)
        print("*"*50)
    elif choice==6:
        n1=int(input("Enter Number : "))
        UDF.pattern(n1)
        print("*"*50)
    elif choice==7:
        print("Thank You.")
        print("*"*50)
        break
    else:
        print("Invalid Choice. Please Try Again.")
        print("*"*50)
        
