import speech_recognition as sr #when we accces speech recognition just mention the sr only
import webbrowser
import pyttsx3

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook"in c.lower():
        webbrowser.open("https://facebook.com")
    elif "youtube"in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open whatsapp"in c.lower():
        webbrowser.open("https://whatsappweb.com")
        
    
if __name__=="__main__":
    speak("Initializing Cyber-Jarvis.....")
    while True:
        #listen for the wake word "Cyber Jarvis"
        #obtain audio from the microphone
        r=sr.Recognizer()
        try:
                with sr.Microphone() as source:
                    print("Listening ...! ")
                    audio=r.listen(source)
                word =r.recognize_google(audio)
                if(word.lower()=="jarvis"):
                    speak("Yes Sir...! How can i Help you..!")
                    #Listen For Command
                    with sr.Microphone() as source:
                        print("Cyber Jarvis Active...")
                        audio=r.listen(source)
                        command =r.recognize_google(audio)
                        processCommand(command)
                        
                        
                        
        except Exception as e:
                print("ERROR :{0}".format(e))
                
        