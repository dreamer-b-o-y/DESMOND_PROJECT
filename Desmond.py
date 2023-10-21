#############################################################
# importing openAI Module and make jarvis like REAL JARVIS  #
# mergin jarvis with chatGPT                                #
# developing JARVIS daily                                   #
#                                                           #
#                                                           #
#                                                           #
#                                                           #
#############################################################





###############################################################
# Some Rules for Desmond kernel (they can be changed if needed)!
#--------------------------------------------------------------
#1- Any command that will be created must be start with the "activation key word" (Desmond). @

#2- please code with keeping the documentation in mind, don't forget to write comments to make it clear and easy for the other developers to collaborat. @

#3- it's a good practice to try the command you just created to see how does Desmond actually heared it and then make a list of every possible macthing word, to make the command take affect from the first time (look at the kernel and you will understand) !!

#4- it's a good practice to put some "dots (..........)" at the speaking voice to avoid the rush in speaking and not understanding what is meant (look at the kernel and you will understand) !!

#5- please try each command you create and test it very will before you push your changes to the (main repo) @

#6- sometimes we are gonna need to nickname things in our code just to reffrence it and access it quicker, so whenver you want to nickname a thing just write a comment with its name and use this format       *[THE NICKNAME]*     for instance =====>   *[The pluged ear]*   ,  and then write its description inside (Brackets)  "look at line 251 and you will understand" !!
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# The signs
#----------

# @ ====> means Mandatory
# !! ====> means it's better to do it (Trust me)
###############################################################







#This is a repo for THE SECRET PROJECT (Desmond PROJECT)

#NOTE: every collaborator in this project "Kindly", must adhere to confidentiality, this project is TOP SECRECT and can't be shown to the public yet since it is a unique idea and we will be the first of our kind to do something like that.

#WHAT IS Desmond?

#Desmond project is not just a virtual assistant in your computer and it's not like [ google_assistane or Cortana or any V.assistante ] Jasper is a "Terminal commands executor" This means that any commands that you can write in your Terminal, can be executed without typing it you can just order Desmond to execute it for you by just saying a verbal command or an oral order.

#It's "Literally" just like Desmond the AI of Tony Stark aka "Iron Man" or at least very close to it.

#Desmond consists of a set of pre-written instructions (commands) that can be executed with just an oral order or a verbal command.



######################################
# the needed modules
#-------------------
import speech_recognition as S_R
import sys
import pyttsx3
import subprocess
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#######################################







#initalizing the voice settings
#------------------------------

engine = pyttsx3.init()

voices = engine.getProperty('voices') # getting the 'voices' property to modify on it
engine.setProperty('voice', voices[0].id) # choosing the voice tune [0] for a man's voice // [1] for a woman's voice
engine.say("hello.........Desmond in your service...........to know more about me just say.......Desmond....introduce")
engine.runAndWait() # running the voice to start speaking













############################
# the varibles
#-------------









#############################










# The kernel of Desmond
#------------------------------

recognizer = S_R.Recognizer()

with S_R.Microphone() as src:

    while True:
        print('Say Something.....')
        audio = recognizer.listen(src)
        text = recognizer.recognize_google(audio)
        print(f"command: {text}")
        print('\n'*2)




    #- The introduction of Jasper -#

        if text in ["Desmond introduce" , "Jervis introduce" , "Desmond introduce"]:
            print("hello i am Desmond, your virtual assistant I'm here to make your computer use easier Just say Desmond....followed by what you want me to do and After completing your command I will still be waiting for the next command, so please when you don't want anything from me, just say.... 'thanks close', for instance........Try to say....  'Desmond open my photos', then say.... 'thanks close' \n and to hear this message again say... 'Desmond again'")
            engine.say("hello..........i am Desmond, your virtual assistant...........I'm here to make your computer use easier............Just say Desmond......followed by what you want me to do.........and After completing your command........I will still be waiting for the next command,..........so please when you don't want anything from me,......just say....thanks...close, for instance........Try to say....Desmond open my photos, then say....thanks...close \n and to hear this message again say...Desmond....again")
            engine.runAndWait()
            print('\n'*2)
        






    #- Repeat The introduction of Desmond -#
        elif text in ["Desmond again" , "Desmond again" , "Desmond again"]:
            engine.say("hello..........i am Desmond, your virtual assistant...........I'm here to make your computer use easier............Just say Desmond......followed by what you want me to do.........and After completing your command........I will be still waiting for the next command,..........so please when you don't want anything from me,.....just say....thanks...close, for instance........Try saying Desmond open my photos, then say....thanks...close \n and to hear this message again say...Desmond....again")
            engine.runAndWait()
            print('\n'*2)







    #- The activation key word ( Desmond ) -#

        elif text in ["Desmond" , "Desmond" , "Desmond"]:
            print('hello Master, what do you want me to do?')
            engine.say("hello Master, what do you want me to do?")
            engine.runAndWait()
            print('\n'*2)
            






    #- Introduction of Desmond creators -#

        elif text == "who created you":
            print("The Ready team created me in 2023 and currently i am still under construction if you want to know more about them you can just reach their GitHub acounts the names are [Abdelrhman helmy , Mohamed Ayman , Yassin Waleed , Ayman Mohamed , Yousra , Omar , Menna] ")
            engine.say("The Ready team created me in 2023 ........ and currently i am still under construction ................ if you want to know more about them you can just reach their GitHub acounts .............. the names are ............ [Abdelrhman helmy ,......... Mohamed Ayman ,........... Yassin Waleed ,.......... Ayman Mohamed ,......... Yousra ,........... Omar ,.......... Menna] ")
            engine.runAndWait()
            print('\n')







    #- Just for kidding -#      
      
        elif text == "tell us more about yourself":
            print("Sure!, i am a prototype for a chat Buddy AI\nAnd i am still under construction so please excuse my slow performance\nAnd finally when i get drunk i really tend to play with 'Netflix' Database (*-*). ")
            engine.say("Sure!, .......... i am a prototype for a chat Buddy A I............................ And i am still under construction so please excuse my slow performance\n................ And finally when i get drunk i really tend to play with 'Netflix' Database.")
            engine.runAndWait()
            print('\n')







#######################################################################################################################
#============ Desmond commands ============#


    #- personal use Desmond commands -#

        elif text in ["Desmond open my photos" , "Desmond open my photos" , "Desmond open my photos" ]:
            print("Working on it...")
            engine.say("Working on it...")
            engine.runAndWait()
            print('\n'*2)
            
            # Specify the path to the file or folder you want to open in File Explorer
            file_or_folder_path = r"C:\Users\body\OneDrive\Wallpapers\wallpaperFlare"

            # Use the 'explorer' command to open the file or folder in File Explorer
            subprocess.Popen(['explorer', file_or_folder_path], shell=True)















        # elif text in ['Desmond WhatsApp' , 'Desmond WhatsApp' , 'Desmond WhatsApp']:            
        #     print('to whom you want to send the WhatsApp message?')
        #     engine.say('to whom you want to send the whats app message?')
        #     engine.runAndWait()
        #     print('\n'*2)


        #     print('Say a contact name.....')
        #     audio = recognizer.listen(src)
        #     contact = recognizer.recognize_google(audio)
        #     print(f"contact name: {contact}")
        #     print('\n'*2)
            
            
        #     # while contact != 'Jack' :

        #     if contact in ['Jack']:

        #         def send_whatsapp_message(phone_number, message):
        #             # Specify the path to the Firefox WebDriver (geckodriver)
        #             driver_path = r'C:\Users\body\Downloads\geckodriver-v0.33.0-win64/geckodriver.exe'

        #             # Initialize the Firefox WebDriver
        #             driver = webdriver.Firefox(executable_path=driver_path)

        #             # Open WhatsApp Web
        #             driver.get("https://web.whatsapp.com/")
        #             time.sleep(15)  # Wait for the user to scan the QR code manually

        #             # Find the chat input field
        #             chat_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')

        #             # Type the phone number (including country code)
        #             chat_input.send_keys(phone_number)
        #             time.sleep(1)
        #             chat_input.send_keys(Keys.ENTER)

        #             # Wait for a while to load the chat
        #             time.sleep(2)

        #             # Type the message
        #             chat_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
        #             chat_input.send_keys(message)
        #             time.sleep(1)

        #             # Send the message
        #             chat_input.send_keys(Keys.ENTER)

        #             # Close the browser
        #             driver.quit()

        #         # Example usage
        #         phone_number = "01020117743"  # Replace with the recipient's phone number
        #         message = "Hello, this is a test message from Python using Firefox!"

        #         send_whatsapp_message(phone_number, message)
        #     else:
        #         print("Sorry i think i didn't get the name right, can you say it again")
        #         engine.say("Sorry....i think i didn't get the name right, can you say it again")
        #         engine.runAndWait()

        #         audio = recognizer.listen(src)
        #         contact = recognizer.recognize_google(audio)
        #         print('Say a contact.....')
        #         print(f"contact name: {contact}")
        #         print('\n'*2)






       











    #- proffesional Desmond commands ( Terminal commands )-#


    

        elif text in "Desmond encrypt":
            print("Working on it...")
            engine.say("Working on it...")
            engine.runAndWait()
            print('\n'*2)
            
            # Specify the path to the file or folder you want to open in File Explorer
            

            # Use the 'explorer' command to open the file or folder in File Explorer
            subprocess.Popen('manage-bde encrypt', shell=True)






#######################################################################################################################


    #- The deactivation key word ( thanks close ) -#
        elif text in "thanks close":
            print("Happy to help Goodbye.")
            engine.say("Happy to help ..... Goodbye.")
            engine.runAndWait()
            sys.exit(0)

            



    #- *[The pluged ear]* (the sentence in case Desmond heared a command or an order that is not inside its database or a command that he simply can't processing it) -#

        else:
            print("Sorry i didn't understand,can you say that again in a more clear voice?")
            engine.say("Sorry i didn't understand,........can you say that again in a more clear voice?")
            engine.runAndWait()