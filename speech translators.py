import speech_recognition as sr
from googletrans import Translator
import pyttsx3

def listen_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {text}")
            return text
        except sr.UnknownValueError:
            print("😕 Could not understand audio.")
            return None
        except sr.RequestError:
            print("❌ Could not request results; check your connection.")
            return None

def translate_text(text, target_lang='es'):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    print(f"🌐 Translated: {translation.text}")
    return translation.text

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print("\nPress Enter to translate or type 'exit' to quit.")
        cmd = input()
        if cmd.lower() == 'exit':
            break
        text = listen_speech()
        if text:
            translated = translate_text(text, 'es')
            speak_text(translated)

if __name__ == "__main__":
    main()
