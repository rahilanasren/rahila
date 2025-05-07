import speech_recognition as sr
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Simulate a basic list of locations and places
locations = {
    "Times Square": "New York, NY",
    "Central Park": "New York, NY",
    "Eiffel Tower": "Paris, France",
    "Colosseum": "Rome, Italy",
    "Sydney Opera House": "Sydney, Australia"
}

nearby_places = {
    "restaurant": ["Joe's Pizza", "The Food Court", "Bistro Café"],
    "gas station": ["Shell", "BP", "Exxon Mobil"],
    "hospital": ["City Hospital", "HealthCare Center", "Medicare Clinic"]
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for commands...")
        speak("How can I assist you?")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        speak("Service error.")
        return None

def get_directions(destination):
    # Simulate directions for known locations
    if destination in locations:
        speak(f"Directions to {destination} are ready. It is located in {locations[destination]}.")
        print(f"Directions to {destination}: {locations[destination]}")
    else:
        speak(f"Sorry, I don't have directions to {destination}. Please try another location.")

def find_nearby_places(query):
    # Find places based on a query (restaurant, gas station, etc.)
    if query in nearby_places:
        speak(f"Found the following {query} nearby:")
        for place in nearby_places[query]:
            print(place)
            speak(f"{place}.")
    else:
        speak(f"Sorry, no {query} found nearby.")

# Main flow
while True:
    command = listen()

    if command:
        if "restaurant" in command.lower():
            find_nearby_places("restaurant")
        elif "gas station" in command.lower():
            find_nearby_places("gas station")
        elif "hospital" in command.lower():
            find_nearby_places("hospital")
        elif "directions to" in command.lower():
            destination = command.lower().replace("directions to", "").strip()
            get_directions(destination)
        elif "exit" in command.lower():
            speak("Goodbye!")
            break
        else:
            speak("I didn't understand the command. Try asking for nearby restaurants, gas stations, or hospitals.")
