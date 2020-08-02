import pyttsx3
import speech_recognition as sr

recognition = sr.Recognizer()
robotMouth  = pyttsx3.init()
robotBrain  = ""

# nhan thong tin
while True:
    # obtain audio from the microphone
    with sr.Microphone() as source:
        print("Say something...")
        robotEar = recognition.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        you = recognition.recognize_google(robotEar)
    except sr.UnknownValueError:
        you = ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    print("You: " + you)

    # hieu thong tin
    if "hello" in you:
        robotBrain = "Hello"
    elif "my love" in you:
        robotBrain = "Lynn"
    elif "bye" in you:
        break
    else:
        robotBrain = "Robot could not understand what you say."

    print("Robot: "+robotBrain);

    # tra loi
    robotMouth.say(robotBrain)
    robotMouth.runAndWait()
