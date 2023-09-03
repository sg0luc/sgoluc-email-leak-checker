"""
Sgoluc Leak Check
Author: Sg0luc
Created: 2023-09-03
Enjoy! :)
"""

import sys
import json
import requests
from pprint import pprint
from sendMessage import sendmessage

# Raw URL: https://leakcheck.io/api?key=YOUR_KEY&check=example@example.com&type=email
# Usage: python leakCheck.py [TYPE]

api_file = open('C:\\Users\\lucas\\OneDrive\\Documents\\Projects\\Keys\\leakcheck_token.txt', 'r')
api_key = api_file.read()

emails_file = open('C:\\Users\\lucas\\OneDrive\\Documents\\Projects\\Keys\\emails.txt', 'r')
emails_list = emails_file.readlines()

search_type = sys.argv[1]

# Arquivo para armazenar informações sobre mensagens enviadas
arquivo_mensagens_enviadas = 'C:\\Users\\lucas\\OneDrive\\Documents\\Projects\\Keys\\mensagens_enviadas.json'

# Inicialize mensagens_enviadas como um dicionário vazio
mensagens_enviadas = {}

# Carregar as informações sobre mensagens enviadas do arquivo, se existirem
try:
    with open(arquivo_mensagens_enviadas, 'r') as arquivo:
        mensagens_enviadas = json.load(arquivo)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    pass

for e in emails_list:
    try:
        request = requests.get('https://leakcheck.io/api?key=' + api_key + '&type=' + search_type + '&check=' + e)
        response = json.loads(request.text)

        for i in response['result']:
            message = 'SGOLUC LEAK CHECK - NOVO VAZAMENTO DETECTADO\nCredencial: ' + i['line'] + '\n'

            # Verifique se 'sources' está presente e não vazio
            if 'sources' in i and i['sources']:
                sources_message = 'Fonte(s): ' + ', '.join(i['sources']) + '\n'
                message += sources_message

            message += 'Último vazamento: ' + i['last_breach']

            # Criar uma chave composta com e-mail, source e data do último vazamento
            chave = (e.strip(), ', '.join(i['sources']), i['last_breach'])

            # Converter a tupla em uma string para usá-la como chave
            chave_str = str(chave)

            # Verificar se a mensagem já foi enviada anteriormente
            if chave_str not in mensagens_enviadas:
                # Enviar a mensagem para o Telegram (ou realize a ação desejada)
                sendmessage(message)
                # Adicionar a mensagem ao dicionário de mensagens enviadas
                mensagens_enviadas[chave_str] = message

    except Exception as e:
        print('Request not sent. Reason:', e)

# Salvar as informações sobre mensagens enviadas de volta no arquivo
with open(arquivo_mensagens_enviadas, 'w') as arquivo:
    json.dump(mensagens_enviadas, arquivo)

