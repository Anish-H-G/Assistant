import speech_recognition as sr 
import datetime 
import subprocess 
import pywhatkit 
import pyttsx3 
import webbrowser


engine=pyttsx3.init() 
voices=engine.getProperty('voices') 
engine.setProperty('voice', voices [1].id) 
recognizer=sr.Recognizer() 

def cmd(): 
    while True:
        with sr.Microphone() as source: 
            print('Clearing background noises.. Please wait') 
            print("\n Listening... (Say 'stop' to exit)")
            recognizer.adjust_for_ambient_noise(source, duration=0.5) 
            print('Ask me anything..') 
            recordedaudio=recognizer.listen(source)
            
        try:
            command=recognizer.recognize_google(recordedaudio).lower()
            print("Message:", format(command))
            
            if "stop" in command:  
                    print(" Stopping voice assistant...")
                    engine.say("Stopping voice assistant.")
                    engine.runAndWait()
                    break

            execute_command(command)
        except Exception as ex:
            print(ex)

def execute_command(command):
    """Executes the recognized command"""            
            
    if 'chrome' in command: 
        a='Opening chrome..' 
        engine.say(a) 
        engine.runAndWait() 
        program="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" 
        subprocess.Popen([program]) 
    elif 'time' in command: 
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time) 
        engine.say(time) 
        engine.runAndWait() 
    elif 'play' in command: 
        b='Opening Youtube' 
        engine.say(b) 
        engine.runAndWait() 
        pywhatkit.playonyt(command)
            
    else:
        print("Command not recognized.")
            
        
cmd()   
        