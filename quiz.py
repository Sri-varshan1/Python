
print ("Welcome to my quiz game !")

playing = input ("Do you want to start? (yes/no) ").lower()
if playing != "yes":
    quit()

score = 0

print ("Okay! Let's play :) ")

answer = input("What does CPU stands for? " )
if answer.lower() == "central processing unit":
    print ("correct!")
    score += 1 
else:
    print ("Incorrect!")    
    print ("It's fine :) The correct answer is central processing unit ")

answer = input("What does RAM stands for? " )
if answer.lower() == "random access memory":
    print ("correct!")
    score += 1
else:
    print ("Incorrect!")    
    print ("It's fine :) The correct answer is random access memory")

answer = input("What does GPU stands for? " )
if answer.lower() == "graphics processing unit":
    print ("correct!")
    score += 1
else:
    print ("Incorrect!")    
    print ("It's fine :) The correct answer is graphics processing unit ")   

answer = input("What does UPS stands for? " )
if answer.lower() == "uninterruptible power supply":
    print ("correct!")
    score += 1
else:
    print ("Incorrect!")    
    print ("It's fine :) The correct answer is uninterruptible power supply")         

answer = input("What does PSU stands for? " )
if answer.lower() == "power supply":
    print ("correct!")
    score += 1
else:
    print ("Incorrect!")    
    print ("It's fine :) The correct answer is power supply")   

answer = input("What does HTML stands for? " )
if answer.lower() == "hypertext markup language":
    print ("correct!")
    score += 1
else:
    print ("Incorrect!")    
    print ("It's fine :) The correct answer is hypertext markup language")

answer = input("What does CSS stands for? " )
if answer.lower() == "cascading style sheet":
    print ("correct!")
    score += 1
else:
    print ("Incorrect!")    
    print ("It's fine :) The correct answer is cascading style sheet")  

answer = input("What does OS stands for? " )
if answer.lower() == "operating system":
    print ("correct!")
    score += 1
else:
    print ("Incorrect!")    
    print ("It's fine :) The correct answer is operating system ")   

answer = input("What does BIOS stands for? " )
if answer.lower() == "basic input/output system":
    print ("correct!")
    score += 1
else:
    print ("Incorrect!")    
    print ("It's fine :) The correct answer is basic input/output system") 

answer = input("What does CD stands for? " )
if answer.lower() == "compact disc":
    print ("correct!")
    score += 1
else:
    print ("Incorrect!")    
    print ("It's fine :) The correct answer is compact disc")                   

print ("You got " + str(score) + " questions correct")    
print ("You got " + str((score / 10) * 100) + " %")      