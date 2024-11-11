print("Hello User Welcome to Simple Calculator")
while (True): 
    opr_input = input("Do you want to continue using calculator ? type (yes/no) : "   ).lower()
    if (opr_input == 'yes'):
        a = float(input("please enter the number : "))
        maths = str(input("select the type of mathematical operation from the list [Addition = '+',Substraction = '-',Division = '/', Multiplication = '*', Modulus = '%', Exponential = '**'] :")).lower()
        b = float(input("please enter the second number :"))
        
        if(maths == '+'):
            print(a+b)
        elif(maths == '-'):
            print(a-b)
        elif(maths == '*'):
            print(a*b)
        elif(maths=='/'):
            print(a/b)
        elif(maths=='%'):
            print(a%b)
        elif(maths=="**"):
            print(a**b)
                    
    
    elif(opr_input == 'no'):
        break