import speech_recognition as sr 

def ouvir_microfone():
    recognizer=sr.Recognizer()

    with sr.Microphone() as source:
        print("Por favor, fale alguma coisa !!")
        recognizer.adjust_for_ambient_noise(source)  # Ajusta para o ruído ambiente
        audio = recognizer.listen(source)  # Escuta o áudio do microfone

    # Usa o reconhecimento de fala do Google para converter o áudio em texto
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
    # Faça o processamento necessário com o texto falado
    # Neste exemplo, estamos apenas exibindo o texto falado
    print("Texto falado:", texto_falado)
