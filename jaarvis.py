import speech_recognition as sr
import webbrowser
import pyttsx3
from spotipy.oauth2 import SpotifyOAuth
from AppOpener import close,open
import json
import spotipy
import requests


def spotify():
    username = 'Zeus'
    clientID = ''
    clientSecret = ''
    redirect_uri = 'http://google.com/callback/'

    # Set up OAuth
    oauth_object = SpotifyOAuth(client_id=clientID, client_secret=clientSecret, redirect_uri=redirect_uri)
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    spotifyObject = spotipy.Spotify(auth=token)
    user_name = spotifyObject.current_user()

    # Print user information
    print(json.dumps(user_name, sort_keys=True, indent=4))

    # Initialize recognizer
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                speak("Spotify initialized. What would you like to do?")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                user_input = command.lower()

            if user_input == "search song":
                with sr.Microphone() as source:
                    speak("What song would you like to search for?")
                    audio = r.listen(source)
                    search_song = r.recognize_google(audio)

                results = spotifyObject.search(search_song.lower(), 1, 0, "track")
                songs_dict = results['tracks']
                song_items = songs_dict['items']

                if song_items:
                    song = song_items[0]['external_urls']['spotify']
                    webbrowser.open(song)
                    speak('Song has opened in your browser.')
                else:
                    speak("No song found with that name.")

            elif user_input == "stop search":
                speak("Good Bye, Have a great day!")
                break

        except Exception as e:
            print(e)

newsapi=""
recogniser=sr.Recognizer()
engine=pyttsx3.init()
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
# engine.setProperty('volume',2.0)
  
# voices = engine.getProperty('voices')       #getting details of current voice
# # #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
engine.setProperty('rate', 180)     # setting up new voice rate

def speak(text):
  engine.say(text)
  engine.runAndWait()
  
def processCommand(c):
  if "open google"in c.lower():
    webbrowser.open("https://google.com")
  elif "open youtube"in c.lower():
    webbrowser.open("https://youtube.com")
  elif "open twitter"in c.lower():
    webbrowser.open("https://twitter.com")
  elif "close google" in c.lower():
    close("chrome") 
  elif "open spotify" in c.lower():
    spotify() 
  elif "open valo" in c.lower():
    open("valorant")
  elif "news" in c.lower():
    r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
    if r.status_code==200:
      data=r.json()
      articles=data.get('articles',[])
      for article in articles:
        speak(article["title"])
        with sr.Microphone() as source:
                  audio = recogniser.listen(source, timeout=2, phrase_time_limit=2)
                  try:
                      stop_command = recogniser.recognize_google(audio).lower()
                      if "stop" in stop_command:
                          speak("Stopping news.")
                          break
                  except sr.UnknownValueError:
                      continue
    else:
       speak("Failed to retrieve news.")
  else:
    speak("do you want to search on google or is it a preexisting command")
    r = sr.Recognizer()
    with sr.Microphone() as source:
                audio = r.listen(source)
                command = r.recognize_google(audio).lower()
                if "no i don't want" in command:
                  speak("speak again! Your command was not clear!")
                else:
                 
                  webbrowser.open(f"https://www.google.com/search?q={c.lower()}&rlz=1C1VDKB_enIN1046IN1046&oq=car&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg7MgYIAhBFGDwyBggDEEUYPDIGCAQQRRhB0gEIMzk3N2owajSoAgCwAgA&sourceid=chrome&ie=UTF-8")
                  
  
if __name__=="__main__":
  speak("Initialising Jarvis")
  
  while True:
  # Listen for wake word "Jarvis"
    r=sr.Recognizer()
    
    print("recognizing...")
    # Recognize speech using Google
    try:
      with sr.Microphone() as source:
       print("Listening...")
       audio=r.listen(source,timeout=2,phrase_time_limit=1)
     
      word=r.recognize_google(audio)
      if(word.lower()=="jarvis"):
        speak("Yes sir!") 
        
        # Listening for command
        with sr.Microphone() as source:
         print("Jarvis Activated!")
         audio=r.listen(source)
         command=r.recognize_google(audio)
          
         processCommand(command)
      if(word.lower()=="band kar"):
        speak("Jarvis down!")
        break 
                
    except  Exception as e:
      print(f"Error;{e}")
