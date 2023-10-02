###############################################################
# Some Rules for JARVIS kernel (they can be changed if needed)!
#--------------------------------------------------------------
#1- Any command that will be created must be start with the "activation key word" (JARVIS). @

#2- please code with keeping the documentation in mind, don't forget to write comments to make it clear and easy for the other developers to collaborat. @

#3- it's a good practice to try the command you just created to see how does JARVIS actually heared it and then make a list of every possible macthing word, to make the command take affect from the first time (look at the kernel and you will understand) !!

#4- it's a good practice to put some "dots (..........)" at the speaking voice to avoid the rush in speaking and not understanding what is meant (look at the kernel and you will understand) !!

#5- please try each command you create and test it very will before you push your changes to the (main repo) @

#6- sometimes we are gonna need to nickname things in our code just to reffrence it and access it quicker, so whenver you want to nickname a thing just write a comment with its name and use this format       *[THE NICKNAME]*     for instance =====>   *[The pluged ear]*   ,  and then write its description inside (Brackets)  "look at line 241 and you will understand" !!
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# The signs
#----------

# @ ====> means Mandatory
# !! ====> means it's better to do it (Trust me)
###############################################################











######################################
# the needed modules
#-------------------
import speech_recognition as S_R
import sys
import pyttsx3
import subprocess
import pyautogui
#######################################







#initalizing the voice settings
#------------------------------

engine = pyttsx3.init()

voices = engine.getProperty('voices') # getting the 'voices' property to modify on it
engine.setProperty('voice', voices[0].id) # choosing the voice tune [0] for a man's voice // [1] for a woman's voice
engine.say("hello.........Jarvis in your service...........to know more about me just say.......Jarvis....introduce")
engine.runAndWait() # running the voice to start speaking













############################
# the varibles
#-------------









#############################










# The kernel of JARVIS
#------------------------------

rec = S_R.Recognizer()

with S_R.Microphone() as src:

    while True:
        print('Say Something.....')
        audio = rec.listen(src)
        text = rec.recognize_google(audio)
        print(text)
        print('\n'*2)




    #- The introduction of JARViS -#

        if text in ["Jarvis introduce" , "Jervis introduce" , "Jarves introduce"]:
            engine.say("hello..........i am Jarvis, your virtual assistant...........I'm here to make your computer use easier............Just say Jarvis......followed by what you want me to do.........and After completing your command........I will still be waiting for the next command,..........so please when you don't want anything from me,......just say....thanks...close, for instance........Try saying Jarvis open my photos, then say....thanks...close \n and to hear this message again say...Jarvis....again")
            engine.runAndWait()
            print(text)
            print('\n'*2)
        






    #- Repeat The introduction of JARViS -#
        elif text in ["Jarvis again" , "Jervis again" , "Jarves again"]:
            engine.say("hello..........i am Jarvis, your virtual assistant...........I'm here to make your computer use easier............Just say Jarvis......followed by what you want me to do.........and After completing your command........I will be still waiting for the next command,..........so please when you don't want anything from me,.....just say....thanks...close, for instance........Try saying Jarvis open my photos, then say....thanks...close \n and to hear this message again say...Jarvis....again")
            engine.runAndWait()
            print(text)
            print('\n'*2)







    #- The activation key word ( JARViS ) -#

        elif text in ["Jarvis" , "Jervis" , "Jarves"]:
            print('hello Master, what do you want me to do?')
            engine.say("hello Master, what do you want me to do?")
            engine.runAndWait()
            print(text)
            print('\n'*2)
            






    #- Introduction of JARVIS creators -#

        elif text == "Jarvis who created you":
            print("The PlaceHolder team created me in 2023 and currently i am still under construction if you want to know more about them you can just reach their GitHub acounts the names are [Abdelrhman helmy , Mohamed Ayman , Yassin Waleed , Ayman Mohamed] ")
            engine.say("The PlaceHolder team created me in 2023 ........ and currently i am still under construction ................ if you want to know more about them you can just reach their GitHub acounts .............. the names are ............ [Abdelrhman helmy ,......... Mohamed Ayman ,........... Yassin Waleed ,.......... Ayman Mohamed] ")
            engine.runAndWait()
            print('\n')







    #- Just for kidding -#      
      
        elif text == "tell us more about yourself":
            print("Sure!, i am a prototype for a chat Buddy AI\nAnd i am still under construction so please excuse my slow performance\nAnd finally when i get drunk i really tend to play with 'Netflix' Database (*-*). ")
            engine.say("Sure!, .......... i am a prototype for a chat Buddy A I ..................\n........... And i am still under construction so please excuse my slow performance\n................ And finally when i get drunk i really tend to play with 'Netflix' Database.")
            engine.runAndWait()
            print('\n')







#######################################################################################################################
#============ JARVIS commands ============#


    #- personal use JARVIS commands -#

        elif text in ["Jarvis open my photos" , "Jervis open my photos" , "Jarves open my photos" ]:
            print("Working on it...")
            engine.say("Working on it...")
            engine.runAndWait()
            print(text)
            print('\n'*2)
            
            # Specify the path to the file or folder you want to open in File Explorer
            file_or_folder_path = "E:\Body\downloads\Egybest"

            # Use the 'explorer' command to open the file or folder in File Explorer
            subprocess.Popen(['explorer', file_or_folder_path], shell=True)













    #- proffesional JARVIS commands ( Terminal commands )-#











#######################################################################################################################3


    #- The deactivation key word ( thanks close ) -#
        elif text in "thanks close":
            print("Happy to help Goodbye.")
            engine.say("Happy to help ..... Goodbye.")
            engine.runAndWait()
            print(text)
            sys.exit(0)

            



    #- *[The pluged ear]* (the sentence in case JARVIS heared a command or an order that is not inside its database or a command that he simply can't processing it) -#

        else:
            print("Sorry i didn't understand,can you say that again in a more clear voice?")
            engine.say("Sorry i didn't understand,........can you say that again in a more clear voice?")
            engine.runAndWait()










