import pyttsx3
import speech_recognition as sr
from prompts.prompt_handler import get_user_prompt
from codegen.generator import generate_code_from_prompt, save_code

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_voice_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return ""

def main():
    print("🎉 Welcome to Scriptly - Your Python Code Assistant")
    speak("Hello! What Python code would you like me to write?")
    
    method = input("Type 'voice' for voice input or 'text' for text input: ").strip().lower()
    if method == 'voice':
        prompt = get_voice_input()
    else:
        prompt = get_user_prompt()
    
    print(f"Generating code for: {prompt}")
    speak("Generating your Python script...")

    code = generate_code_from_prompt(prompt)
    print("\nGenerated Code:\n")
    print(code)

    save_code(prompt, code)
    speak("Done. Your code has been saved to the output folder.")

if __name__ == "__main__":
    main()
