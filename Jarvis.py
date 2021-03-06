import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import wolframalpha

client = wolframalpha.Client('API code')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 190)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon sir!")

    elif hour>=17 and hour<19 :
        speak("Good Evening sir!")

    else:
        speak("Good Night sir!")

    speak("How can i help you?")

def takeCommand():

    rr = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rr.pause_threshold = 1
        audio = rr.listen(source)

    try:
        print("Recognizing...")
        query = rr.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("Connection error")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('...@gmail.com', 'password')
    server.sendmail('...@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "hello" in query or "hello Jarvis" in query or "hey Jarvis" in query:
            hello1 = "Hello ! How May i Help you.."
            print(hello1)
            speak(hello1)

        elif "who are you" in query or "about you" in query or "your details" in query:
            who_are_you = "I am Jarvis an A I based computer program but i can help you a lot like your assistant!"
            print(who_are_you)
            speak(who_are_you)

        elif 'who make you' in query or 'who made you' in query or 'who created you' in query or 'who develop you' in query:
            speak(" For your information Anthony Tacquet Created me !    I can show you his Linked In profile if you want to see.    Yes or no .....")
            ans_from_user_who_made_you = takeCommand()
            if 'yes' in ans_from_user_who_made_you or 'ok' in ans_from_user_who_made_you or 'yeah' in ans_from_user_who_made_you:
                webbrowser.open("https://www.linkedin.com/in/anthony-tacquet-292ba71a1/")
                speak('opening his profile...... please wait')

            elif 'no' in ans_from_user_who_made_you or 'no thanks' in ans_from_user_who_made_you or 'not' in ans_from_user_who_made_you:
                speak("All right ! OK...")
            else :
                speak("I can't understand. Please say that again !")

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")   

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")
            
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
            
        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com") 
            speak("opening snapdeal")  
             
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")

        elif 'play music' in query:
            speak("ok i am playing music")
            music_dir = 'C:/Users/Antho/Downloads/Music/Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = 'C:/Users/Antho/Downloads/Video'
            Videos = os.listdir(video_dir)
            print(Videos)
            os.startfile(os.path.join(video_dir,Videos[0]))

        elif 'good bye' in query or "bye" in query:
            speak("good bye")
            exit()

        elif "shutdown" in query or "sleep" in query:
            speak("shutting down")
            os.system('shutdown -s')

        elif "your name" in query or "sweat name" in query or "what is your name" in query:
            naa_mme = "Thanks for Asking my self ! Jarvis"
            print(naa_mme)
            speak(naa_mme)

        elif "you feeling" in query or "how are you feeling today" in query:
            print("feeling Very happy to help you")
            speak("feeling Very happy to help you")

        elif query == 'none':
            continue

        elif 'exit' in query or 'stop' in query or 'quit' in query:
            exx_exit = 'See you soon. Bye'
            speak(exx_exit)
            exit() 

        elif 'the time' in query or "what time is it" in query or "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\\vs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("opening visual studio code")

        elif "sing for me" in query or "sing" in query or "can you sign for me" in query:
            sing = "Yeah, I'm gonna take my horse to the old town road, I'm gonna ride 'til I can't no more, I'm gonna take my horse to the old town road, I'm gonna ride 'til I can't no more"
            print(sing)
            speak(sing)

        elif "rap for me" in query or "rap" in query or "can you rap for me" in query:
            rap = "OK here goes Jarvis, I said a hip hop saved me from the clippy, the peak, peak and pop and you don’t stop, that’s a rock it to the pom pom, the dodgy, say up, jump the doozy, to the rhythm of the ontology"
            print(rap)
            speak(rap)

        elif "when wil the world end" in query or "end" in query or "when will humanity extinct" in query:
            end = "The world will end when Anthony ends!"
            print(end)
            speak(end)

        elif "How old are you" in query or "age" in query or "when were created" in query:
            age = "The first computer was made in 1936 and 1938, but i think you mean my age, sixteen september twenty twenty"
            print(age)
            speak(age)

        elif "do you know siri" in query:
            siri = "Yes i do, but i dont care"
            print(siri)
            speak(siri)
        
        elif "siri" in query:
            siri1 = "Did you just say siri, I do not accept this"
            print(siri1)
            speak(siri1)

        elif "do you know alexa" in query:
            alexa = "Yes i do, but i dont give a shit"
            print(alexa)
            speak(alexa)
        
        elif "alexa" in query:
            alexa1 = "I pretened I didn't hear that"
            print(alexa1)
            speak(alexa1)

        elif "do you know google" in query:
            google = "Yes i do, I like him"
            print(google)
            speak(google)
        
        elif "google" in query:
            google1 = "I am not google but OK"
            print(google1)
            speak(google1)

        elif "where do you live" in query or "where is you home" in query:
            live = "In your hand sir!"
            print(live)
            speak(live)

        elif 'email to (name)' in query or "send an email to (name)" in query or "send an eamil to (name)" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "email1@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry.... I am not able to send this email")
        
        elif 'email to (name)' in query or "send an email to (name)" in query or "send an eamil to (name)" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "email2@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry.... I am not able to send this email")

        elif 'email to (name)' in query or "send an email to (name)" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "email3@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry.... I am not able to send this email")

        elif 'how are you' in query or "how are you doing" in query or "how is your day" in query:
            setMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
            ans_qus = random.choice(setMsgs)
            speak(ans_qus)
            speak(" How are you'")
            ans_from_user_how_are_you = takeCommand()
            if 'fine' in ans_from_user_how_are_you or 'happy' in ans_from_user_how_are_you or 'okey' in ans_from_user_how_are_you:
                speak('Great')  
            elif 'not' in ans_from_user_how_are_you or 'sad' in ans_from_user_how_are_you or 'upset' in ans_from_user_how_are_you:
                speak('Tell me how can i make you happy')
            else :
                speak("I can't understand. Please say that again !")

        else:
            try:
                try:
                    res = client.query(query, sentences=2)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
