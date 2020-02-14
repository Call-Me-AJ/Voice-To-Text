import speech_recognition as sr
a=sr.Recognizer()
with sr.Microphone() as speech:
    print("listening....")
    spoke=a.listen(speech)
    text=a.recognize_google(spoke)
    while True:
        if "exit" in text:
            print("ok")
            break
        else:
            print(text)
            print()
            print("listening....")
            spoke=a.listen(speech)
            text=a.recognize_google(spoke)
