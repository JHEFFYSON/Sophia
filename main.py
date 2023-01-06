import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser


listener = sr.Recognizer()
maquina = pyttsx3.init()
voices = maquina.getProperty('voices')
maquina.setProperty('voice', voices[1].id)
maquina.setProperty('rate', 150) 
command = 0

def comando_voz(text):
    maquina.say(text)
    maquina.runAndWait()


def comando_voz_usuario(): 
    global command 
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voices = listener.listen(source)
            command = listener.recognize_google(voices,language='pt-BR')
            command = command.lower()
            if 'Sophia ' in command:
                command = command.replace('Sophia ', '')
        
    except sr.RequestError:
        print('Desculpe, buguei!')
        comando_voz('Desculpe, buguei!')
        
    except:
        pass

    return command

    
def run_Sophia():
    command = comando_voz_usuario()
    print('Eu:', command)

    if 'tocar' in command:
        musica = command.replace('tocar', '')
        comando_voz('Tocando' + musica)
        print('Tocando' + musica)
        pywhatkit.playonyt(musica)

    elif 'pesquise' in command:
        pesquise = command.replace('pesquise', '')
        url = 'https://google.com/search?q=' + pesquise
        webbrowser.get().open(url)
        print('Aqui está o que eu encontrei para ' + pesquise)
        comando_voz('Aqui está o que eu encontrei para ' + pesquise)

    elif 'mapa' in command:
        localiacao = command.replace('mapa', '')
        url = 'https://google.nl/maps/place/' + localiacao + '/&amp;'
        webbrowser.get().open(url)
        print('Aqui está o mapa de ' + localiacao)
        comando_voz('Aqui está o mapa de ' + localiacao)

    elif 'hora' in command:
        hora = datetime.datetime.now().strftime('%I:%m %p')
        print(hora)
        comando_voz('A hora atual é ' + hora)

    elif 'fale sobre' in command:
        ask = command.replace('fale sobre', '')
        info = wikipedia.summary(ask, 2)
        print(info)
        comando_voz(info)

    elif 'como vai você' in command:
        comando_voz('Estou bem. Obrigada! E você?')

    elif 'o que você está fazendo' in command:
        comando_voz('hmmm.. estou muito ocupada')

    elif 'Piada' in command:
        Piada = pyjokes.get_joke()
        print(Piada)
        comando_voz(Piada)

    elif 'Quem é Você' in command:
        comando_voz('Eu sou a Sophia. Sua assistente virtual. se você está entediado, posso contar uma piada, posso reproduzir vídeos do youtube para você e blá, blá e eu sou incrível.')
    elif 'obrigado' in command:
        comando_voz('De nada. Mais alguma coisa que você quer que eu faça?')

    elif 'tchau' in command:
        comando_voz('tchau. Até mais.')

    elif 'sair' in command:
        exit()

    else:
        print('Desculpe, eu não entendi isso')
        comando_voz('Desculpe, não entendi')

while True:     
    run_Sophia()
