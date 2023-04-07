import json
import re
from flask import Flask, request, abort, make_response
import requests
import openai
from openai_key import key

def generate_text(json_demo, short_answer, recomendacion):
    
    texto = ""
    if False:
        texto = r"""
¡Hola! Gracias por contactarnos en KAVAK. Me he dado cuenta de que eres un comprador y, en base a tus registros, podríamos ofrecerte algunos autos que podrían ajustarse con tus gustos y expectativas. 

Primero que nada, noté que eres una mujer joven y activa, lo que nos lleva a recomendarte un carro dinámico y ágil. A su vez, veo que en tu historial de compras has adquirido autos de un rango de precio alto, por lo que es posible que estés buscando algo con una gama de opciones más amplia. 

Tenemos excelentes opciones en nuestra plataforma, desde marcas de prestigio como Audi y BMW, hasta modelos más juveniles como el Mazda 2 o el Suzuki Swift.

Si te gustaría considerar más opciones, te sugiero que eches un vistazo al Honda City, Honda Fit, Honda Civic y al modelo que te haya gustado más. Además, al ser un cliente calificado, podemos ofrecerte excelentes alternativas de financiamiento personalizadas a tus necesidades y en condiciones justas.

¿Te gustaría agendar una cita para ver nuestros vehículos de cerca y descubrir más ventajas de comprar en KAVAK? ¡Nuestra plataforma está aquí para ayudarte en lo que necesites!                    
        """
    else:
        openai.api_key = key

        mensaje = """
                Te envio los datos del cliente en formato Json a continuación.

                """+json_demo+"""
                
                Cómo puedes ver, el json contiene varias variables con datos del cliente, como por ejemplo 
                el long term value del usuario, su semento, su nivel de ingresos, etc. 

                Analiza los campos del json para poder entender que tipo de cliente tenemos y genera un texto
                como si fueses una persona del equipo de ventas que está atendiendo a este cliente.

                Hay un campo muy importante que es el message_history en donde puedes obtener la lista completa
                de los mensajes que se han enviado con el usuario y el equipo de ventas.

                Lo que quiero que hagas es basarte en el historial del usuario y en sus variables  y darme un 
                parrafo de ventas amigable, para empatizar con el usuario en si próximo contacto con el equipo
                
        """

        if recomendacion:
            mensaje = mensaje + """
            
            Quiero que hagan énfasis en una recomendación de un auto o dos autos, basado en lo que has visto del historial.
            
            """
        else:
            mensaje = mensaje + """
            
            En el parrafo que generes, no quiero que recomiendes ningún auto.
            
            """

        if short_answer:
            mensaje = mensaje + """
            
            Que sea una respuesta pequeña de solo un parrafo.
            
            """


        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": mensaje}]
        ).choices[0].message
        texto = completion["content"]

    texto = texto.replace('\n', '<br>')
    return texto

#Obtiene la tabla de usuarios y la guarda en el array
my_array = []
with open('example.json', 'r') as file:
    for line in file:
        json_data = json.loads(line)
        my_array.append(json_data)
print("Populated users ")

#Obtiene la tabla de usuarios y la guarda en el array
my_dict = {}
with open('example_calls.json', 'r') as file:
    for line in file:
        #obtiene los datos del row
        json_data = json.loads(line)

        #obtener el teléfono y buscarlo en el mapa
        tel = json_data['phone_ten_digits']
        
        if tel not in my_dict:
            #si no está, agregar la clave con el texto
            my_dict[tel] = json_data['wmd_message']
        else:
            #si está, obtener el contenido del texto, apendearle el nuevo y guardarlo
            previous_text = my_dict[tel]
            new_text = previous_text + "\n" + json_data['wmd_message']
            my_dict[tel] = new_text
        
print("Populated calls")        
        
new_tel = 2291145836
print("tel: "+str(new_tel))
print("messages: ---------------------")
print(my_dict[str(new_tel)])

#Crea el server
print("Creating server...")

app = Flask(__name__)

@app.route('/users')
def show_user_info():
    print("request received")
    email = request.args.get('email')

    recomendacion = True
    if request.args.get('recomendacion')=='false':
        recomendacion = False

    short_answer = True
    if request.args.get('short')=='false':
        short_answer = False

    for json_data in my_array:
        if email in json_data['ten_digit_phone+email']:

            #recorta el mail del telefono+mail para dejar solo el tel
            tel_plus_email = json_data['ten_digit_phone+email']
            tel = tel_plus_email.replace(email,"").strip()

            #si no hay teléfono, tira not found
            if tel == "":
                abort(404)        
            
            #obtiene el historial de mensajes y lo agrega al json
            if tel in my_dict:
                json_data['message_history'] = my_dict[tel]            
            else:
                #harcoded for the demo
                json_data['message_history'] = my_dict[str(new_tel)]

            #llamar a la función que conecta con el chat gpt y pasarle el json y el prompt
            json_string = json.dumps(json_data)
            respuesta = generate_text(json_string, short_answer, recomendacion)

            # Convertir el diccionario a JSON con encoding utf-8
            json_data = json.dumps(respuesta, ensure_ascii=False).encode('utf8')
            
            # Crear una respuesta HTTP con el JSON y el header de allow cors
            response = make_response(json_data)
            response.headers.set('Content-Type', 'application/json')
            response.headers.set('Access-Control-Allow-Origin', '*')            
            print(json_data)
            return response
    
    abort(404)

if __name__ == '__main__':
    app.run()

