import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    engine = pyttsx3.init()
    
    while True:
        x = input("Enter what you want the system to speak (or type 'exit' to quit): ")
        if x.lower() == 'exit':
            print("Exiting RoboSpeaker.....")
            engine.say("Exiting RoboSpeaker.")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
