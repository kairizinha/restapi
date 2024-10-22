import requests
from flask import Flask, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/obter_dados', methods=['GET'])
def obter_dados():
    url = "https://www.w3schools.com/xml/note.xml"  # Exemplo XML
    response = requests.get(url)

    if response.status_code == 200:
        # Processar o conteúdo XML
        xml_data = response.content
        root = ET.fromstring(xml_data)

        # Extrair informações específicas
        note_data = {
            'to': root.find('to').text,
            'from': root.find('from').text,
            'heading': root.find('heading').text,
            'body': root.find('body').text
        }

        return jsonify(note_data), 200
    else:
        return jsonify({'error': 'Falha ao obter dados'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)