
import random

list = ['"rustam"','"anshu"','"mr.gopal"','"mrs.mohini"','"school"','"student"' ]
    
    
print(list)
    
print("write only in small letters! \n write same word as list \n let's go: ")
    
print("Choose a word or number that is choise by computer! ")
    
computer = random.choice([1,2,3,4,5,6])
you = input("Enter a name that computer has guess: ")
    


youdict = {
        "rustam" : 1,
        "anshu" : 2,
        "mrs.mohini" : 3,
        "mr.gopal" : 4,
        "school" : 5,
        "student" : 6 
    }
youstr = youdict[you]
reverse_dict = {
        1 : "rustam",
        2: "anshu",
        3: "mrs.mohini",
        4:"mr.gopal",
        5:"school",
        6:"student"
    }
    
print(f"you choose {reverse_dict[youstr]} \n computer chose {reverse_dict[computer]}")
    

if(computer == youstr ):
    print("congratulatons🎉, You found")
else:
    print("Try again please!")

