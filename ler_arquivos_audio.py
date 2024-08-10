import speech_recognition as sr

rec = sr.Recognizer()

#passe o arquivo ou caminho 

with sr.AudioFile("audio.wav") as arquivo_audio:
    try:
        audio = rec.record(arquivo_audio)


        texto = rec.recognize_google(audio, language="pt-BR")

        print(texto)
    except:
        print("Não identifiquei o áudio")
