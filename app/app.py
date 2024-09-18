import os
import json


def handler(event, context):

    datos_json=event["body"]
    print("AQUI 1")

    evento=json.loads(datos_json)


    # try:
    #     update_colletions(datos)
    #     return {'statusCode': 200, 'body': str("result")}
    # except:
    #     return {'statusCode': 400, 'body': str("Error en la carga de datos")}
