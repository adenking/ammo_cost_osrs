import requests


# this is the main file designed to be run
def GE_Request(ammo_names):
    prices = {}
    for ammo in ammo_names:
        r = requests.get('http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=' +
                         str(ammo_names[ammo]))
        prices[ammo] = r.json()['item']['current']['price']
    return prices


if __name__ == '__main__':
    # define all arrows, bolts and darts
    arrow_names = {'Bronze arrow': 882, 'Iron arrow': 884, 'Steel arrow': 886, 'Mithril arrow': 888,
                   'Adamant arrow': 890, 'Rune arrow': 892, 'Amethyst arrow': 21326}
    # TODO add amethyst and dragon arrows with ids
    # TODO add bolts and darts
    # get GE prices of items
    arrow_prices = GE_Request(arrow_names)

    # determine broken ammo of used ammo
    backpacks = {'assembler': .20, 'accumulator': .28}

    # display cost per shot
    print('Cost Per Shot')
    for backpack in backpacks:
        print(f'{backpack}:')
        for arrow in arrow_prices:
            print(f'{arrow}: {arrow_prices[arrow]*backpacks[backpack]}')
    # determine fire rate
    tick = 0.6
    weapon_fire_rate = {'shortbow': 4, 'longbow': 6}
    for weapon in weapon_fire_rate:
        for backpack in backpacks:
            print(backpack)
            for arrow in arrow_prices:
                print(f'{weapon}, {arrow} cost per minute: {(arrow_prices[arrow]*backpacks[backpack])*(60/(tick*weapon_fire_rate[weapon]))} GP')
    # determine cost per minute/hour
