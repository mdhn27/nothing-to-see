import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://wetterstation.physik.rwth-aachen.de/aktuelle_daten.php"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

text = soup.get_text()

temp = re.search(r"Temperatur:\s*([0-9.]+)", text).group(1)
humidity = re.search(r"Luftfeuchte:\s*([0-9.]+)", text).group(1)
wind = re.search(r"Windgeschwindigkeit:\s*([0-9.]+)", text).group(1)

data = {
    "temperature_c": float(temp),
    "humidity_percent": float(humidity),
    "wind_m_s": float(wind)
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
