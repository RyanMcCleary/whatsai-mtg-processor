import sys
import requests

def get_card_details(card_name):
    url = f'https://api.scryfall.com/cards/named?fuzzy={card_name}'
    headers = {
        'Accept': '*/*',
        'User-Agent': 'WhatsAI MTG Card Processor version 0.0'
    }
    response = requests.get(url, headers = headers)

    if response.status_code != 200:
        return 'Error:\n' + str(response.json().get('details'))

    data = response.json()

    name = data.get('name', 'N/A')
    mana_cost = 'N/A'
    if 'mana_cost' in data:
        mana_cost = data['mana_cost'].replace('}{', ' ').lstrip('{').rstrip('}')
    type_line = data.get('type_line', 'N/A')
    oracle_text = data.get('oracle_text', 'N/A')
    flavor_text = data.get('flavor_text', 'None')

    power = data.get('power')
    toughness = data.get('toughness')
    pt = f'{power}/{toughness}' if power and toughness else 'N/A'

    details = f'''
Name: {name}
Mana Cost: {mana_cost}
Type: {type_line}
Power/Toughness: {pt}
Oracle Text: {oracle_text}
Flavor Text: {flavor_text}
'''
    return details.strip()

if __name__ == '__main__':
    card_name = sys.argv[1]
    print(get_card_details(card_name))
