import speech_recognition as sr 

def ouvir_microfone():
    recognizer=sr.Recognizer()

    with sr.Microphone() as source:
        print("Por favor, fale alguma coisa !!")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)  
    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse: " + texto)
        return texto
    except sr.UnknownValueError:
        print("Não foi possível reconhecer a fala.")
    except sr.RequestError as e:
        print("Erro ao conectar-se ao serviço de reconhecimento de fala: {0}".format(e))

    return None

texto_falado = ouvir_microfone()

if texto_falado:

    print("Texto falado:", texto_falado)
