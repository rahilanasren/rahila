import speech_recognition as sr

# Mock function to control appliances
def control_appliance(command):
    if "turn on the light" in command:
        print("Turning on the light...")
    elif "turn off the light" in command:
        print("Turning off the light...")
    elif "set temperature" in command:
        print("Setting temperature...")
    else:
        print("Command not recognized.")

def main():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        try:
            # Adjust for ambient noise and capture speech
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            print("Recognizing...")
            
            # Convert speech to text
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            
            # Control the appliance based on the command
            control_appliance(command.lower())
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    main()
