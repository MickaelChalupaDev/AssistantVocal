import sys
import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("voice", 'french')
engine.setProperty("rate", 200)
voices = engine.getProperty('voices')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def greetMe():
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
        talk('Bonjour !')

    if 12 <= current_hour < 18:
        talk('Bon après midi !')

    if current_hour >= 18 and current_hour != 0:
        talk('Bonsoir !')

# definition de la voix française
greetMe()
#engine.say('comment vas tu?')
engine.say('Que puis je faire pour toi?')
engine.runAndWait()
engine.setProperty('voice', voices[0].id)
def assistant_command():
    with sr.Microphone() as source:

        print("En train d'écouter...")
        listener.pause_threshold = 1
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language="fr")
        command = command.lower()
        print(command)
        if 'assistant' in command:
            command = command.replace('assistant', '')
            print(command)
    return command

def run_assistant():
    command = assistant_command()
    if 'musique' in command:
        chanson = command.replace('musique de', '')
        talk('musique en cours de lecture....')
        pywhatkit.playonyt(chanson)
        print(song)
    elif 'quelle heure est-il' in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk('il est actuelement: ' + time)
    elif 'qui est' in command:
        person = command.replace("qui est", "")
        wikipedia.set_lang("fr")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "sortir" in command:
        talk("Désolé, je suis un peu souffrante en ce moment.")
    elif "es-tu en couple" in command:
        talk("non pas encore, mon coeur est encore à conquérir.")
    elif "blague" in command:
        jokes = [
            "Comment appelle-t-on un cochon homo?… «Alors ? «Tu ne sais pas?» «Un porc tout gay...»",
            "Sais-tu quel est la différence en une femme et un ascenceur?»… «Aucune»… «Tu mets ton doigt ou t'habite»",
            "Comment appelle-t-on une course a pied de somalien? «Une course de cotes»",
             ]
        talk(random.choice(jokes))
    elif "et toi" in command:
        msgs = ["Je fais juste mon truc !", "Je vais bien !", "Bien !", "Je suis bien et plein d'énergie."]
        talk(random.choice(msgs))
    elif "désactive toi" in command:
        talk("merci de m'avoir utilisé !")
        sys.exit()
 
    elif "dehors" in command:
        talk("Mais attend, tu me prend pour un thermomètre moi! J'en sais foutre rien! Tu n'a qu'a sortir un peu")
    elif "parle pas" in command:
        talk("Je te parle comme j'ai envie")
    else:
        talk("pourrais tu repété? je n'ai pas bien compris.")

if __name__ == '__main__':
    while True:
        run_assistant()
