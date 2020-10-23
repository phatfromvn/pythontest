import pyttsx3
import speech_recognition as sr
import os
from subprocess import call

recognition = sr.Recognizer()
robotMouth  = pyttsx3.init()
robotBrain  = ""

def robotReply(robotBrain):
    print("Robot: "+robotBrain);
    robotMouth.say(robotBrain)
    robotMouth.runAndWait()

# nhan thong tin
while True:
    # obtain audio from the microphone
    with sr.Microphone() as source:
        print("Robot: Say something.")
        robotEar = recognition.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        you = recognition.recognize_google(robotEar)
    except sr.UnknownValueError:
        you = ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    you = input("You: 123")

    # hieu thong tin
    if "hello" in you:
        robotBrain = "Hello"
    elif "my love" in you:
        robotBrain = "Lynn"
    elif "notepad" in you:
        robotBrain = "opening notepad."
        os.system('notepad.exe')
    elif "vs code" in you:
        call(["C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"])
    elif "chrome" in you:
        call(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
    elif "sleep" in you:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif "bye" in you:
        robotBrain = "Bye"
    else:
        robotBrain = "Robot could not understand what you say."

    # tra loi
    robotReply(robotBrain)
# xx
# zz