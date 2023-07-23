from flask import Flask, render_template
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def abrir_microfone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Por favor, fale alguma coisa!!")
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

@app.route('/abrir_microfone_callback', methods=['POST'])
def abrir_microfone_callback():
    texto_falado = abrir_microfone()
    if texto_falado:
        return texto_falado

@app.route('/minimizar_janela', methods=['POST'])
def minimizar_janela():
    # Implement minimization logic here
    return "Minimized"

@app.route('/fechar_janela', methods=['POST'])
def fechar_janela():
    # Implement window closing logic here
    return "Closed"

if __name__ == "__main__":
    app.run(debug=True)
