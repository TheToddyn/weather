import requests


def obter_informacoes_clima(cidade):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=6161ce7ee60e813d42d1a895a211b327"
    response = requests.get(url)
    dados_clima = response.json()

    # Extrair as informações relevantes do JSON
    temperatura = dados_clima.get('main', {}).get('temp')
    if temperatura is None:
        temperatura = 'N/A'
    descricao = dados_clima.get('weather', [{}])[0].get('description')

    # Retornar as informações do clima
    latitude = dados_clima.get('coord', {}).get('lat')
    longitude = dados_clima.get('coord', {}).get('lon')
    return temperatura, descricao, latitude, longitude


def traduzir_clima(descricao):
    traducoes = {
        'clear sky': 'céu limpo',
        'few clouds': 'poucas nuvens',
        'scattered clouds': 'nuvens dispersas',
        'broken clouds': 'entre nuvens',
        'shower rain': 'chuva fraca',
        'rain': 'chuva',
        'thunderstorm': 'trovoada',
        'snow': 'neve',
        'mist': 'névoa'
    }
    return traducoes.get(descricao, 'desconhecido')


cidade = input("Digite o nome da cidade: ")
temperatura, descricao, latitude, longitude = obter_informacoes_clima(cidade)
temperatura = round(float(temperatura) - 273.15, 2)
descricao_traduzida = traduzir_clima(descricao)
print(f"A temperatura em {cidade} é de {temperatura}°C. O clima está {descricao_traduzida}.")
