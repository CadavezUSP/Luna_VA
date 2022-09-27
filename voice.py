from functions import *

mode = int(input("1-voz\n2-texto\n"))
while True:
    comando = takeCommand(mode=mode).lower()

    if "abrir youtube" in comando:
        SpeakText("Abrindo youtube mestre")
        webbrowser.open("youtube.com")

    elif "tocar" in comando:
        #! arrumar !!!!
        tocar_deezer(comando)



    elif 'wikipédia' in comando:
        SpeakText('buscando na Wikipedia...')
        searchWiki(comando)

    elif "abrir google" in comando:
        SpeakText("Abrindo google mestre")
        webbrowser.open("google.com")
        
    elif 'abrir deezer' in comando or "abrir dizer" in comando:
        open_play_deezer(comando)

    elif "aonde fica" in comando:
        where_is(comando)
        
    elif "qual é o tempo em" in comando or "qual é a temperatura em" in comando:
        find_weather(comando)

    elif "calcular" in comando:
        wolfram_calc(comando)

    elif "o que é" in comando or "quem é" in comando:
        wolfram_who(comando)
    
    elif "matéria " in comando:
        abrir_materia(comando.replace("matéria ",""))
    elif "conte uma piada" in comando:
        joke = pyjokes.get_joke(language="en")
        print(joke)
        SpeakText(joke, "en")

    elif "traduzir para" in comando:
        traduzir(comando)

    elif "hibernar" in comando:
        # SpeakText("que soninho, adeus mestre")
        os.system("terminator -x dormir")

    elif "reiniciar" in comando:
        SpeakText("reiniciando, adeus mestre")
        os.system("terminator -x shutdown -r 0")

    elif "desligar" in comando:
        SpeakText("desligando, adeus mestre")
        os.system("terminator -x shutdown 0")
    elif "sair" in comando:
        exit()

    elif "assistir kaguya-sama" in comando:
        webbrowser.open("https://www.anitube.site/892862/")