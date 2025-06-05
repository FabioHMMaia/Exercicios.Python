a = int(input("When you are born? "))
b = int(input("What year is it? "))
idade = b - a

def year(a,b):
    if (b - a):
        return(print(f"You have {idade} years old"))
    else:
        return(print("NO LOCATADED"))

result = year(a,b)
