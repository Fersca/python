import base64
import html
import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def getHtml(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        # Aquí puedes procesar el contenido HTML
        return html_content
    else:
        print(f"Error al obtener la página: {response.status_code}")
        return ""

def contenido_a_codigo(jsonContent):

    posicion_inicio = jsonContent.find("base64,")   
    recorte = jsonContent[posicion_inicio+8:] 
    posicion_final = recorte.find("\"")
    recorte = recorte[:posicion_final] 
    return recorte

def codigo_a_imagen(datos_base64):
    
    # Convertir entidades HTML en caracteres normales
    datos_base64_scapeado = html.unescape(datos_base64)
    # Decodificar la cadena base64
    datos_imagen = base64.b64decode(datos_base64_scapeado)
    archivo_path = "/Users/Fernando.Scasserra/code/python/imagen_salida.png"
    # Escribir los datos a un archivo PNG
    with open(archivo_path, "wb") as archivo:
        archivo.write(datos_imagen)
    #print("Imagen guardada como 'imagen_salida.png'")
    return archivo_path

def imagen_a_texto(archivo):
    # Especifica la ruta de Tesseract si no está en PATH
    pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

    try:
        # Cargar la imagen
        imagen = Image.open(archivo)
        # Aplicar OCR a la imagen
        texto = pytesseract.image_to_string(imagen)
    except IOError:
        print(f"No se pudo abrir la imagen en la ruta: {archivo}")
    except pytesseract.pytesseract.TesseractError as e:
        print(f"Error en Tesseract: {e}")

    return texto

def procesa_codigo_e2e(jsonContent):
    codigo = contenido_a_codigo(jsonContent)
    archivo = codigo_a_imagen(codigo)
    numero = imagen_a_texto(archivo)
    return numero

jsonContent = """
{
    "htmlContent": "\n<div class=\"contact-details\">\n    <p>N&#xFA;mero de tel&#xE9;fono del vendedor</p>\n    <div class=\"phone-number\">\n            <img src=\"data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAHkAAAAcCAYAAABFwxCgAAAABHNCSVQICAgIfAhkiAAABvVJREFUaIHtWU1oJMcV/l5192W0PRN86QRvDp2uHl&#x2B;CHBOfIoFP3s0PxArsEkJIgqVcDDGs4uBAwnrxgrFvKxJIyEEShkAwNkG&#x2B;2N7bhnh1WogtQsAzPbQJ8aGPo9HMZVVVPqhqUtPqnu62bJ/6O01Vv3nfe1WvXr2qAlq0aNGiRYsWLVp8KSC7EQTBSqfTiQDAcZxpkiSjKgWc80gIsVKDK0vTNGvCVUP3gk4ACMMwABCYdpqmRzVsK0QYhqvm92w2G2VZNq1pV6l9RbqL/LfHJ8/fFK5R2O12f0lEO/bHfr9/IKX8zbLJJqLfe573bBWRlHILwF4Trirdtk7f99cZYzcBrNkycRyPALwyHA73q2y0wTnfZIztmnan03kcwFEdu/L2mXYYhque5/0pb6NSah/AJjCfi18T0W1bptvtjrrdbmM/AIBpBX/MD7rGBhHdtaPuovgiuHzf/zFj7D3kBg8AiCgioj3O&#x2B;bW6&#x2B;sIwDOwJ/jzAOd/0PO/DIhtt&#x2B;L7/Qn6CgQU/bjTldqMoWiMiOyoPlVIfmT4iijzPexnAj4oUKKWOAJyLLiJ6DMB3rK5PLsh1qJT6KNf3CQBMJpM3er3eluZLlVL3tL45F2PsBoC3inzIw3XdV5d9b&#x2B;IzcLaCc0GTKqXuKaWOiGhV6zPB9bLFs6&#x2B;Uep8x9kMAz2iOXwEoWiTl/mjD5uTj8fhKlmVTzvk7jLE3df8G5zwqSttJkhQScs5fYowZhw&#x2B;TJLnLOd9swmVPkpRyN0mSPRQgy7Jpp9N5znGcJ20ZzvkRY&#x2B;yObi5dQdZ/ruUC8Rya&#x2B;AwAruvOV59Sav/4&#x2B;Pj5kv01sBunp6c7aZoehWH4wPM8M8lRwf&#x2B;WghHRumXAPUOeJEk&#x2B;6p&#x2B;oqzQfkVLKXW3gZ&#x2B;YiIj8Mw9WydJ6m6VFZEGgc1rGbiF6rkiv7b5HPnPPIDprj4&#x2B;Pnfd//ahiGq5zzhQmbzWYLi8h13WfCMAx0dqvtRx6uUupjorMim4j65kPeAADdukodx/mJ3Z5MJm8AwEW4iGjH8zwA5cWUqaxd1/02gMv23ialPLfP5eF53m8BRFr&#x2B;lj1pVSjzGQC3ug96vd5fAWwwxowve6enp79L0zTLsmzq&#x2B;/62yT5EdNvzvAW7hRAv1rXJwAXwH6u9FsfxLoCPAfyiqTLgrDrU&#x2B;waAs8GyUlNtLj1hhdApa49zTvbqdRznB0UFk5TyukmdZYiiaA3ANnCWUoUQB3UnucLnRy3RjQJfNj3PewS6DkmSZCeO49WiLUNKeX00Gt2vY5MNNplM3gWQ2qREdDuf&#x2B;wuKnkL4vr9u/1cIcWB&#x2B;N&#x2B;GazWYnUspbOCtS9vUx4&#x2B;0F42tWwIyxG3oSCxEEwQpj7HWL/5U6eg2W&#x2B;Qzgck78UEq5jcW0u2Hs45xfLasJiOi1gqxXCZZl2VRK&#x2B;TTO5/qFAZVSTmopZOwlW4d9GdGEK8uyaZIktweDwTeGw&#x2B;HmcDjcHAwGG/rsOYe9RwshHkgpt6SUWzooDNYYY6&#x2B;XZQd9bIkAQCm1J4RYcV03tmVc143L6oFlPjPGvmLLjsfjK0mS7IzH4yt2PxE9pqvw92xdUsrr0AtDH6PuBkFQ5yLm/7YDgK6a18xNjuM4UyHEiqnogPNFQRF0NM6PEFLKP&#x2B;dlLsq1LKPowTUDvBdF0a7jOO8DZwPkOM63AJxL23Za1ulzMy9DRG/pmmDhlrDKZynlv83&#x2B;q5Sa31plWTbt9XoLHI7jPGm7MxgMNgCAc/4vxlhi/PB9/3tZltU6DgL6MsQgSZJRmqZHQogTu6LL7THlyhizV1m6bB&#x2B;s4uKcX&#x2B;WcX63gAICMc36tKI0R0deqbL4oqny2g5KIIpMNCrLKMWPsm1b7Q/NDLww7&#x2B;9UuggG9kjnnNxhjX1dK/RfAKhEtRLIQ4i9VivJHBSnlH0rk6nI9yhjb7ff7UEqZ4uqp3P79dpqmWRzH3yeiN/v9/n0zqET0CHKFjhDigyKb8luAxuXckegWgP819fnk5OSDXq&#x2B;XAggBwHXdv8dx/A8AT&#x2B;Vs&#x2B;ycAMMa2dddGHMc3Nec6rGwhhHhQ5EcZXAAgolUAz5rjjYVUSvlc2SV7Dj/NGf23IqHPwpUPBAMp5Qu5rjUiKiywpJRbZX4Una/1/jifZCHEQcFjR6XPWZZNL1269DN724A&#x2B;plm2badpmgVB8G6v1zuEntCi600Ad5o&#x2B;urCyD0qpfSnl01VHD2BendrHjTs1A6OUS0dr4cFfKbX/8OHDx80NnFLqnTJZnFWz3624KGmMJj6PRqP7Qoj1IhullFvmBk0Xpj/PFY0LsuPx&#x2B;GZTWwlYfDqr&#x2B;8RoI/8shiVPbE258s96y57cCp4AS&#x2B;2oQtVTXxOfbdgV&#x2B;rIVmX8yvchTY4sWLVq0aNGiRYsWLVq0qI1PAdy2/58YhnCkAAAAAElFTkSuQmCC\" alt=\"Seller phone number\"/>\n    </div>\n</div>\n",
    "trackingData": null,
    "shouldInitVerifyPhoneForm": false,
    "userData": null,
    "debugData": null
}
"""

jsonContent2 = """
{"htmlContent":"\n<div class=\"contact-details\">\n    <p>N&#xFA;mero de tel&#xE9;fono del vendedor</p>\n    <div class=\"phone-number\">\n            <img src=\"data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAHkAAAAcCAYAAABFwxCgAAAABHNCSVQICAgIfAhkiAAABTdJREFUaIHtmT&#x2B;IHUUcx3&#x2B;/md3mzrcpF0ksxp1duzss9QUCQrx0XqFYWIjvBAkoJChYiIQEEsUmQUlhcXdoKRZJIeYaMZC7yiYpBN&#x2B;bx4qYYsuXl7tmMzMWt3vOze2&#x2B;7Ow9Y7MfeLAz892Z3/fN7uz8Aejo6Ojo6Ojo6HgmoJkIw3BxYWEhAgCglO4KIcZtK2aMLZXXe3t74yzLdttqGWMhAIRN6&#x2B;OcR1LKRQDI0jTNnoWHWXojnjqOxOnqeRYewH7nBkHwPiLeMAuTJLmllPrEtbM55wNCyHqZXlhYWAaAB65axljoed41RByY95w4cQKCIBiMRqNNq64VRLyJiBEhpPSwrZR697/08DQ9In7m&#x2B;/57dfcqpdYAYKON5yYQAIAgCL6xO7hgFRG3zCf0aTDGQtNsWy3nfMXzvG3bbAkibnDOL5TpKIr6hJA7iBhZ0n7hIYSGuHhoo6/D1XNTSBRFfUQ0n7IdrfXB04KIke/7l5tW6HneF/PQaq0fWx12KK4itg/La0rpV0ZRanuglH4wj7jmoN/RWm&#x2B;aPwB4CODuuSkEEV8y0ulkMnl9NBoNlFJvGfmrnHP7DTkC5/xN64FprR2Px9tKqXMAkCqlzg2Hw34R11qpQcSIMbZUxPZqma&#x2B;UOl9oLx4YJeRyGIazvovOHprqzXKl1PpoNBqYPyHElqvnpvEB7Hfy6TKhtf61/LgLIX60tC/PqogxFiLil00abaoVQmzlef5K&#x2B;ScUPDQ1lNJdADhj5k2n03sAAFLKX8z8clJ53Lja6gEAELHHGFuq6ygHz40hWus/jQCS8rrizQ1mVeT7/qflUKOUujQvrT3rRMS3jeRO1YTKmIUeupdS&#x2B;vy84mqjBwBAxBu&#x2B;79/3ff9&#x2B;HMcijuMjo0Abz7MgAPC7ke7Hcbwex/HniLhVd5NNFEV9ALgIAKC13pRS3pqH1oZzPrCGvuvF5akqfcXy6eS84mqqnzXhQ8SomExVTrQAZnpuDJlOpz8DQGo0PEDEK/YsVWv9R1UFYRguEkK&#x2B;M3RX6xpz0dpwzlfMGazWerPik9IK17hc9Ht7e4&#x2B;Ltzw1Jlq3Tc2sFcY8PHtZlu32er2zhJDvwZi8FIG8USaUUtOqCnq93sflA6G13pBSLnqeFx9qxPNixhhQSlebatM0PViTFmbvmLE9evToIyP9d1VsFW/Rwyqdi4c0TR&#x2B;46rMsuwIAV8xye13NGFty9NyYQzte5c4MpXRXSrno&#x2B;/79smwymTxXteOSJIlu0/DTGA6HWMR0xOxkMnnHjMX&#x2B;w8pYGWNLpoc8z5fNP7KNh&#x2B;FwiK76qvwoivqU0ntVsTXx7AIxE0KIcZqmD6SUj821sVLqUtsGjoOD2btmotfrnQYAoJS&#x2B;Zulab3G2hXO&#x2B;wjlfsfMJIWtWVlbq59nBAMW2Juf8AiHkBa31XwCwZO&#x2B;4SCm/ravAXMMZnCKEHHpIoGZIrdNyziNEvGlpdRAEXwfBvxN9rfUPQoitJEkOPi&#x2B;IeDOO47uWj&#x2B;t1&#x2B;9iuHhz1Jwkh60mSgNZ6oyg&#x2B;Y815bqdpmrl6rvJSBQIAxHG8UbOgT5VS510qBNj/vjQZJmdp7SG4DqXUmhBiwx7&#x2B;bB95nq/WxXBcD8f1oZTiQoixq&#x2B;emXkhdgdZ6Uyl11rWD/y/G4/F2nufLYKwUClKl1FmXDp4nUsrfAGCnqkxrvZnn&#x2B;fJxTvua4BWNXX3y5MkNgOMfMQLsH4sVpzAHaVetlPInKeVy3X0GB0Nw0ZEvzuOo0cXDLH0RU98&#x2B;bqw6OmzjuaOjo6Ojo6Ojo6Ojo2Ou/AM7EqULKEn7rwAAAABJRU5ErkJggg==\" alt=\"Seller phone number\"/>\n    </div>\n        <div class=\"phone-number\">\n                <img src=\"data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAHkAAAAcCAYAAABFwxCgAAAABHNCSVQICAgIfAhkiAAABpJJREFUaIHtmUGIJEkVhv8XmXnpnsoULymsHtKKLC9ag&#x2B;DF7YE57TYiOC24iAwqW&#x2B;NlwYFdV7wsu8M0KN62WdHFQ3dfFmRVZOakfVtxp0&#x2B;CTCPCVkWRi7hgHrNqui5FRnjoiNqo6MzqyukeT/mdMiJevoh4LyPi5QugpaWlpaWlpaXl/wLZhTiONzc2NroA4HneqRBivI4Sznm3LMvNFSJ5lmV5XWOSJH3zXNVvkiQxgNiUZ7PZOM/z0ypd9hwukl2FPSZXxxrzNSzNu4l9n9YXVfhGYRiGPyKiPbux1&#x2B;s9kFL&#x2B;9KIOiOiNIAhermuXUt4BcGDXJUnSD4LgNwC27Hql1CGAgZaJfd//BRENbJkoihCG4WA0Gh2aOj2HnxDRri0bhuE4DMOf27KrqNKzsbFxHcDJuvN1593Evpf1RRUMAMIw/JWrVLNDREf2V30VcM4HQRA8huNgR2bb9/1HroMNRHTAOX/VlDudzuuug7Vc15WtI47jzSiK3qvScxma2PdZ&#x2B;MLvdrtbRGR/lcdKqY9MHRF1gyC4D&#x2B;Dba&#x2B;o8Vkp95NR9Yh6SJOkzxvattkwp9YFS6oSI&#x2B;kqpEwBQSj1hjHUtuaVx6bH9GMBekiQxY&#x2B;y&#x2B;qVdKHSqlPmSMfQvALVu2btCc8y4RHQHo1slY&#x2B;k8AnNsZiOhLAJ63593Evs/AF2fj4pwPLKNnRVF8Jc/zU875dxhjfzCCUkpet1X0ej1lyd0RQhxUyQFAmqYHZtBKqcPJZHK37szknG8zxt6VUr4ihDjSdfZ4MZ/PrwOA3hkWdVmWnegjYVE/HA6XYhBDkiRxEAT/rRuz0VfXbo33LetjOx4Oh1tN7Avg5mV9UQUjohumoJT6wBhcCPFHR/ar6ygkok6SJP2qbUWvlsWXOplM7nY6nc8lSdLnnJ9bQUKIo/l8/nXjYM0ntozneaez2Wxpwr7v39KOu29VH9eNOcuyXEp5TxcfSilfumCa53B3EynlPgA0se9V&#x2B;8LAlFIfmwIR9cxzhdHDdRQS0V4QBI&#x2B;DIHicpqlI09Tefrj1/CCKovcYYyIIgseMMZGm6b6OpBe4UTkRfdcqHgshxnmen0opX7NkdvXK3DF1ZVn&#x2B;bNW4hRC7Usp7RVHcLstyuM5cbTzP&#x2B;55dnk6n7wNAE/tetS8MPoB/WeWtNE33AXwM4IfrKHCdYkNEXQAHnHPSW/hzVvNOhfwgCILPoubM4ZwP7J1ASvm2eRZC7KVp2nfONCP30ng8fnTRXIQQu3pOF4kuEcfxpj7zTX/3rCOoiX0v5Ys62HQ6/TOAzFQQ0YCIdrWDFlQEUwCA2Wz2RG91mQ54DgE8XOrk03Pm887rx3oF2lvpTrfbPRd16/N5cRYrpQ7tbYxzvl3lYD2nX1YdB1dFp9O5YdurLMsH5rmJfS/rizqY3upewPkza8lRUspplYI8z0&#x2B;FELvD4fCLo9FoMBqNBsPhcEf/Iy7QUfVn7LqiKF4UQuwVRfGiXa&#x2B;j1AXawX&#x2B;xxzaZTO46upfa9bmaaX1dIjqK43idBEZjGGNv2X3bQVoT&#x2B;17WF3X4AKAjtS2TyfE877Qsy80gCG4ZQTe4uYiqr01K&#x2B;U/GmGlfZJHyPD&#x2B;NoqhST5WDi6K4bUfknud9zWrPhsPhjn73H4wxAZw5utPpfCPPczeIuRR611n8Nkkp33Vlmtj3WfiCuYPJsuykLMsndmTqnDFLcM63Oefb5xQzdsepym3HE1HXROAV5/rE6L7IwbqvL1vFxS&#x2B;TNpi9KhoFLOvgzDNz/gSWaGLfp/FFHT4AcM5fZYx9QSn1bwB9N8tUluVvV&#x2B;h4jjG23&#x2B;v1oJQy/8c3nXPkYZZleRzHT6IoygAkAOD7/p/SNP0rgJtOf3/Tv1u/dvpSYRi&#x2B;E4af&#x2B;kop9Xsp5TFjzETXO2mavgngPwBuwFplZVn&#x2B;fbU5muH&#x2B;Ekop36mRW9u&#x2B;l/RFJT4AEFEfwMtE53IFmZTylVWXCzZ1KUgp5evA2bZ87dq173ue96GW78LJMEkpX8uyLOecf9MNOHCW2luqUEo9mk6n70dRdAzt0Jq05NvrJDQactsulGX5uyqhJva9Kl/YsLoGpdShlPKFVdsPsFgdlYkGpdThfD6/bmdnxuPxo7Isb1S9o7NltanHOnTA8gMd2Z9DSnmnKIo3m&#x2B;pdRRzHm3byA2cf0doOWNe&#x2B;TWWrIGD56uxpr7Xc67d1rvjsrJi7ytzrxRUsXec1uZasY53rSlfGHYdNE/tehS9aWlpaWlpaWlpaWlpanpr/AcZjOdI142JmAAAAAElFTkSuQmCC\" alt=\"Seller secondary phone number\"/>\n        </div>\n</div>\n","trackingData":null,"shouldInitVerifyPhoneForm":false,"userData":null,"debugData":null}
"""

#telefono = procesa_codigo_e2e(jsonContent)
#print("Telefono: "+str(telefono))

# Ruta al ChromeDriver
# ruta_chromedriver = '/Users/Fernando.Scasserra/Downloads/chromedriver'  # Cambia esto por la ruta real a tu ChromeDriver
ruta_geckodriver = "/Users/Fernando.Scasserra/Downloads/geckodriver"

#para bajar el mismo chrome:
#https://vikyd.github.io/download-chromium-history-version/#/

# Configura el servicio con la ruta del ChromeDriver
servicio = Service(ruta_geckodriver)

# Inicializa el navegador con el servicio
#navegador = webdriver.Chrome(service=servicio)
navegador = webdriver.Firefox(service=servicio)

navegador.get('https://www.kavak.com/')

#navegador.quit()


