import pyttsx3
import os
import pyfiglet

line1 = pyfiglet.figlet_format("___________________", font = "small")
print(line1)
result = pyfiglet.figlet_format(" SYSTEM ASSISTANT ", font = "slant")
print(result)
line2 = pyfiglet.figlet_format("___________________", font = "small")
print(line2)

print("Heyaa!! I'am HIMSS..How can I help you ? \n")
pyttsx3.speak("Heyaa!! I'am HIMSS..How can I help you ?")
print()

while True:
    print("What you want me to do?")
    pyttsx3.speak('What you want me to do?')
    print("Ask me anything according to your requirements : ",end='')
    p=input()

    if (("run" in p) or ("launch" in p) or ("execute"in p) or ("open" in p)) and ("notepad"in p):
        pyttsx3.speak("opening notepad")
        os.system("notepad")
        
    elif(("run" in p)or("launch" in p)or("execute"in p)or("open" in p)) and ("Notepad++"in p):
        pyttsx3.speak("opening Notepad++")
        os.system("Notepad++")
        
    elif(("run" in p)or("launch" in p)or("execute"in p)or("open" in p)) and ("chrome"in p):
        pyttsx3.speak("opening chrome")
        os.system("chrome")
        
    elif(("run" in p)or("launch" in p)or("execute"in p)or("open" in p)) and ("prompt"in p): 
        pyttsx3.speak("opening command prompt")
        os.system("cmd")

    elif(("run" in p)or("launch" in p)or("execute"in p)or("open" in p)) and ("MicrosoftEdge"in p): 
        pyttsx3.speak("opening MicrosoftEdge")
        os.system("MicrosoftEdge")
        
    elif(("run" in p)or("launch" in p)or("execute"in p)or("open" in p)) and ("paint" in p): 
        pyttsx3.speak("opening paint")
        os.system("paint")
        
    elif("exit"in p)or("quit"in p):
        print("Thank You !!!")
        pyttsx3.speak("Thank You !!!")
        break
    else:
        print("Invalid request")
        pyttsx3.speak("Invalid request")
print()
