print("Welcome to my game!")
playing = input("Do you wanna play? ")

if playing.lower() != "yes" :
    print("ok then bye")
    quit()
    
    
print("Ok then, let's play this!!!")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit" :
    print("well done mate, it's correct")
    score += 1
else: 
    print("it's incorrect!")
    score -= 1
    
    
answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit" :
    print("well done mate, it's correct")
    score += 1
else: 
    print("it's incorrect!")
    score -= 1
    
    
    
answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory" :
    print("well done mate, it's correct")
    score += 1
else: 
    print("it's incorrect!")
    score -= 1
    
    
answer = input("what does PSU stand for? ")
if answer.lower() == "power supply" :
    print("well done mate, it's correct")
    score += 1
else: 
    print("it's incorrect!")
    score -= 1
   
if score >= 0 :
    print("your score is " + str(score) + ", well done!")
    
else:
    print("your score is " + str(score) + ", you fucked up idiot!")