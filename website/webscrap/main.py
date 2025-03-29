import requests
from bs4 import BeautifulSoup

URL="https://resultados.bajasaebrasil.net/prova.php?id=25BR_GER"

req = requests.get(URL)

if req.status_code == 200:
    soup = BeautifulSoup(req.text, 'html.parser')

    table = soup.find(id="myTable")

    data = []
    for line in table.tbody.children:
        if "Baja Guaicurus" in line.text:
            i = 0
            for field in line.children:
                if i == 0 or i == 10:
                    data.append(field.text)

                i += 1

    print(f"Posição: {data[0]}")
    print(f"Pontuação: {data[1]}")
