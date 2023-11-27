# Algortimo para conversão de moedas

import requests


def obter_taxas_de_cambio(api_key):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'

    try:
        params = {'apikey': api_key}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if response.status_code == 200 and 'conversion_rates' in data:
            return data['conversion_rates']
        else:
            print(f'Erro ao obter taxas de câmbio: {data.get("error", "Erro desconhecido")}')
            return {}
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    return {}

def converter_moeda(valor, moeda_origem, moeda_destino, taxas):
    if moeda_origem not in taxas or moeda_destino not in taxas:
        print('Moeda não suportada.')
        return None

    taxa_origem = taxas[moeda_origem]
    taxa_destino = taxas[moeda_destino]

    resultado = valor * (taxa_destino / taxa_origem)
    return resultado


# Insira sua chave de API obtida após o registro no ExchangeRate-API
api_key = '27fbc05db1df99be343b2ff6'
taxas_de_cambio = obter_taxas_de_cambio(api_key)

if taxas_de_cambio:
    # Solicitar entrada do usuário
    valor_a_converter = float(input("Digite a quantia a ser convertida: "))
    moeda_origem = input("Digite a moeda de origem (por exemplo, USD): ").upper()
    moeda_destino = input("Digite a moeda de destino (por exemplo, EUR): ").upper()

    resultado = converter_moeda(valor_a_converter, moeda_origem, moeda_destino, taxas_de_cambio)

    if resultado is not None:
        print(f'{valor_a_converter} {moeda_origem} equivalem a {resultado:.2f} {moeda_destino}')


