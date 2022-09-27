from imports import *


cl_deezer = deezer.Client()
deezer_path = "/snap/bin/deezer-unofficial-player"
translator = Translator(service_urls=['translate.googleapis.com'])
mic_name = "default"
sample= 16000
chunk_size = 1048
mic_list = sr.Microphone.list_microphone_names()
# print(mic_list)

def SpeakText(command,lang="pt"):
     
    # Initialize the engine
    engine = pyttsx3.init()
    if lang == 'pt':
        engine.setProperty('voice', 'brazil+f3')
    else:
        engine.setProperty('voice', 'english_rp+f3' )
    engine.setProperty("rate", 160)
    engine.say(command)
    engine.runAndWait()

for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i

def takeCommand(lang="pt-BR", mode=1):
    if (mode ==1):
        r = sr.Recognizer()
        with sr.Microphone(device_index= device_id, sample_rate=sample, chunk_size=chunk_size) as source:
            print("escutando")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, 0.5)
            audio = r.listen(source)
            try:
                print("Reconhecendo...")   
                query = r.recognize_google(audio, language =lang)
                print(f"você disse: {query}\n")

            except Exception as e:
                print(e)   
                print("Não consegui entender o que você disse")
                # SpeakText("Não consegui entender o que você disse") 
                return "None"
    else:
        query = input()
     
    return query

def getLatLong(city):
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(city) +'?format=json'
    response = requests.get(url).json()
    return response[0]["lat"], response[0]["lon"]

def searchWiki(comando):
    if "buscar na wikipédia" in comando:
        comando = comando.replace("buscar na wikipédia", "")
    else:
        comando = comando.replace("buscar no wikipédia", "")
    wikipedia.set_lang("pt")
    results = wikipedia.summary(comando, sentences = 3)
    SpeakText("De acordo com a Wikipedia")
    print(results)
    SpeakText(results)

def find_weather(comando):
    # Google Open weather website
    # to get API of Open weather
    api_key = google_api
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    if "qual é a temperatura em " in comando:
        city_name = comando.replace("qual é a temperatura em", "")
    else:
        city_name = comando.replace("qual é o tempo em", "")
    Lat, Long = getLatLong(city_name)
    complete_url = base_url + "lat=" + Lat + "&lon=" + Long + "&lang=pt" +"&appid=" + api_key
    response = requests.get(complete_url)
    x = response.json()
    # print(x)
        
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" temperatura (°C) = " +str(round(current_temperature - 273,1))+"\n pressao atm (em hPa) ="+str(current_pressure) +"\n humidade (%) = " +str(current_humidiy)+"%" +"\n descrição = " +str(weather_description))
        txt = "a temperatura é de "+str(round(current_temperature - 273,2)) + "graus celsius"
        SpeakText(txt)
        SpeakText("com "+weather_description)
    else:
        SpeakText("Cidade não encontrada")

def wolfram_calc(comando):
    comando = pyautogui.prompt("o que deseja calcular, em ingles")
    comando = ". " + comando
    app_id =wolf_api
    client = wolframalpha.Client(app_id)
    indx = comando.lower().split().index(".")
    comando = comando.split()[indx + 1:]
    res = client.query(' '.join(comando))
    answer = next(res.results).text
    pyautogui.alert("a resposta é \n" + answer)
    print("a resposta é \n" + answer)
    SpeakText("a resposta é " + answer)

def wolfram_who(comando):
    # Use the same API key
    # that we have generated earlier
    client = wolframalpha.Client(wolf_api)
    _, comando = comando.split("é ")
    comando = translator.translate(comando, src="pt", dest="en")
    res = client.query(comando)
    try:
        print (next(res.results).text)
        SpeakText (next(res.results).text)
    except StopIteration:
        print ("No results")

def tocar_deezer(comando):
    os.system("terminator -xH "+deezer_path)
    comando = comando.replace("tocar", "")
    sleep(15)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write(comando)
    pyautogui.press("enter")
    sleep(2)
    pyautogui.moveTo(297,465)
    location = pyautogui.center(pyautogui.locateOnScreen("./find.png"))
    # print(location)
    pyautogui.moveTo(location[0],location[1])
    sleep(1)
    pyautogui.mouseDown()
    sleep(0.2)
    pyautogui.mouseUp()

def open_play_deezer(comando):
    SpeakText("abrindo deezer")
    os.system("termisnator -xH "+deezer_path)
    # cl_deezer.search(track="Dear")
    

def where_is(comando):
    comando = comando.replace("aonde fica ", "")
    location = comando
    SpeakText("Mestre pediu para localizar")
    SpeakText(location)
    webbrowser.open("https://www.google.nl/maps/place/" + location + "")

def lang_abv(lingua):
    lang = translator.translate(lingua, dest="en", src="pt")
    if lang.text.lower() in LANGCODES:
        return LANGCODES[lang.text.lower()]

def abrir_materia(materia):
    if "web" in materia:
        webbrowser.open("https://edisciplinas.usp.br/course/view.php?id=95999")
    else:
        SpeakText("não encontrei a materia solicitada")

def traduzir(comando):
    lingua = comando.replace("traduzir para ", "")
    SpeakText("o que deseja traduzir")
    print("o que deseja traduzir")
    comando = input()
    lingua = lang_abv(lingua)
    traducao = translator.translate(text=comando, src="pt", dest=lingua)
    print(traducao.text)
    SpeakText(traducao.text)