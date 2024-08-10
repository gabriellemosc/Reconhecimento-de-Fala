# Arquivos de áudio - raw, wav, aiff, flac

import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as microfone:
  rec.adjust_for_ambient_noise(microfone)
  print("Pode começar a falar")
  audio = rec.listen(microfone)


  #Salvar audio
with open("audio.wav", "wb") as arquivo:       #passar o arquivo para escrever "w" e "b" para ser em binário
  arquivo.write(audio.get_wav_data()) 