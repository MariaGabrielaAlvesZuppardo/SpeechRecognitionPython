import tkinter as tk
import speech_recognition as sr

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

def abrir_microfone_callback():
    texto_falado = abrir_microfone()
    if texto_falado:
        texto_falado_label.config(text="Texto falado: " + texto_falado)

def minimizar_janela():
    window.iconify()

def fechar_janela():
    window.destroy()

if __name__ == "__main__":
    # Cria a janela principal
    window = tk.Tk()
    window.title("Conversor de fala em texto")

    # Remove a barra de título padrão
    window.overrideredirect(True)

    # Cria uma frame para o cabeçalho da página
    header_frame = tk.Frame(window, bg="#F8F8FF")
    header_frame.pack(anchor="nw", fill="x")

    # Cria botão para minimizar a janela
    minimizar_button = tk.Button(header_frame, text="-", font=("Arial", 16), command=minimizar_janela)
    minimizar_button.pack(side="left", padx=10)

    # Cria botão para fechar a janela
    fechar_button = tk.Button(header_frame, text="X", font=("Arial", 16), command=fechar_janela)
    fechar_button.pack(side="left", padx=10)

    # Cria um rótulo para exibir o texto falado
    texto_falado_label = tk.Label(window, text="Texto falado:", font=("Arial", 24), bg="#F8F8FF")
    texto_falado_label.pack(pady=50, anchor="center")

    # Cria um botão para iniciar a escuta do microfone
    abrir_microfone_button = tk.Button(window, text="Abrir Microfone", font=("Arial", 24), command=abrir_microfone_callback, bg="#4caf50", fg="white")
    abrir_microfone_button.pack(pady=50, anchor="center")

    # Inicia o loop principal da janela
    window.mainloop()
