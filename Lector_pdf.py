
import PyPDF2
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def extraer_texto_pdf(ruta_pdf):
    texto = ""
    try:
        with open(ruta_pdf, 'rb') as archivo:
            lector = PyPDF2.PdfReader(archivo)
            for pagina in lector.pages:
                texto += pagina.extract_text()
        return texto
    except Exception as e:
        print("Error al leer el PDF:", e)
        return ""

def resumir_texto(texto, num_oraciones=5):
    try:
        parser = PlaintextParser.from_string(texto, Tokenizer("spanish"))
        resumen = LsaSummarizer()
        oraciones = resumen(parser.document, num_oraciones)
        return " ".join(str(oracion) for oracion in oraciones)
    except Exception as e:
        print("Error al generar resumen:", e)
        return ""

if __name__ == "__main__":
    print("=== LECTOR DE PDF Y RESUMIDOR ===")
    ruta = input("Ingresa la ruta del archivo PDF: ").strip()

    texto_completo = extraer_texto_pdf(ruta)

    if texto_completo:
        print("\nTexto extraído exitosamente. Generando resumen...\n")
        resumen = resumir_texto(texto_completo, num_oraciones=5)
        print("=== Resumen ===\n")
        print(resumen)
    else:
        print("No se pudo extraer texto del PDF.")