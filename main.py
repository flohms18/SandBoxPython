import random as rd 

def main():
    MyDicto = {}
    for i in range (1,100):
        MyDicto[i] = {
            "User" : rd.randint(1,100),
            "Name" : rd.randint(1,100)
        }
        print(MyDicto[i]["User"])

main()