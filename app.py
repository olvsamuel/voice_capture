import speech_recognition as sr
import re

def extrair_dados(texto):
    texto = texto.lower()

    # entrada de voz: categoria, valor
    padrao = re.search(r'([\w\s]+?)[, ]+(r\$)?\s*(\d+[,.]?\d*)', texto)

    if padrao:
        categoria = padrao.group(1).strip()
        valor = float(padrao.group(3).replace(',', '.'))
        return categoria, valor
    else:
        return None, None


def ouvir_e_processar():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as fonte:
        print("Pode falar (ex: 'jantar 50 reais')...")
        reconhecedor.adjust_for_ambient_noise(fonte)
        audio = reconhecedor.listen(fonte)

    try:
        texto = reconhecedor.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {texto}")

        categoria, valor = extrair_dados(texto)
        print("Dados extraídos:")
        if categoria and valor:
            print(f"Categoria: {categoria}")
            print(f"Valor: R${valor:.2f}")
            # Trata os dados como tu quiser
        else:
            print("Não consegui entender a categoria ou o valor.")

    except sr.UnknownValueError:
        print("Não entendi o que foi dito.")
    except sr.RequestError as e:
        print(f"Erro ao se comunicar com o serviço de reconhecimento: {e}")

# Rodar
ouvir_e_processar()
