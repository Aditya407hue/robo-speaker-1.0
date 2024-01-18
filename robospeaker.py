import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

speak.Speak("Hello i am robospeaker")
while True:
    x = input("Enter what you want to say:")
    if x== 'q':
        break
    speak.Speak(x)