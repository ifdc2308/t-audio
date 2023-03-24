#pip install playsound #pip install gTTS
from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'pt-br'

sp = gTTS(
    text='Olá, meu nome é Code, sou um exemplo de transcrição de texto feito para demonstrar mais uma das ferramentas que podem ser implementadas em diversos níveis de sistemas',
    lang=language
)
sp.save(audio)
playsound(audio)
