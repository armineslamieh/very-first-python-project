print("Welcome to my game mother fucker!")
playing = input("Do you wanna play? ")

if playing.lower() != "yes" :
    print("go fuck your self")
    quit()
    
    
print("Ok then, let's fucking play this shit!!!")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit" :
    print("well done mate, it's correct")
    score += 1
else: 
    print("it's incorrect idiot!")
    score -= 1
    
    
answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit" :
    print("well done mate, it's correct")
    score += 1
else: 
    print("it's incorrect idiot!")
    score -= 1
    
    
    
answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory" :
    print("well done mate, it's correct")
    score += 1
else: 
    print("it's incorrect idiot!")
    score -= 1
    
    
answer = input("what does PSU stand for? ")
if answer.lower() == "power supply" :
    print("well done mate, it's correct")
    score += 1
else: 
    print("it's incorrect idiot!")
    score -= 1
   
if score >= 0 :
    print("your score is " + str(score) + ", well done mother fucker!")
    
else:
    print("your score is " + str(score) + ", you fucked up idiot!")