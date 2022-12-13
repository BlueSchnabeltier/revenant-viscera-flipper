from json import load
from math import trunc
from time import sleep
from urllib.request import urlopen

if ((float(load(urlopen("https://api.hypixel.net/skyblock/bazaar"))["products"]["REVENANT_FLESH"]["sell_summary"][0]["pricePerUnit"]) + 0.1) * 128) + ((float(load(urlopen("https://api.hypixel.net/skyblock/bazaar"))["products"]["ENCHANTED_STRING"]["sell_summary"][0]["pricePerUnit"]) + 0.1) * 32) > float(load(urlopen("https://api.hypixel.net/skyblock/bazaar"))["products"]["REVENANT_VISCERA"]["buy_summary"][0]["pricePerUnit"]):
    print("\u001b[31mFlipping is not profitable right now! Exiting...\033[0m\n")
    sleep(3)
    exit()

def english():
    while True:
        balance = float(input("How much money do you have? "))
        revenant_flesh_price = float(load(urlopen("https://api.hypixel.net/skyblock/bazaar"))["products"]["REVENANT_FLESH"]["sell_summary"][0]["pricePerUnit"]) + 0.1
        enchanted_string_price = float(load(urlopen("https://api.hypixel.net/skyblock/bazaar"))["products"]["ENCHANTED_STRING"]["sell_summary"][0]["pricePerUnit"]) + 0.1
        revenant_viscera_sell_price = float(load(urlopen("https://api.hypixel.net/skyblock/bazaar"))["products"]["REVENANT_VISCERA"]["buy_summary"][0]["pricePerUnit"])
        revenant_viscera_craft_price = (revenant_flesh_price * 128) + (enchanted_string_price * 32)
        can_craft_count = int(balance / revenant_viscera_craft_price)
        estimated_profit = int(can_craft_count * (revenant_viscera_sell_price - revenant_viscera_craft_price))

        if can_craft_count * 128 > 71680:
            revenant_flesh_print_line = f"""Revenant Flesh 71680x Orders: {trunc(can_craft_count * 128 / 71680)}
Revenant Flesh Rest Order: {round(((can_craft_count * 128 / 71680) - trunc(can_craft_count * 128 / 71680)) * 71680)}"""

        else:
            revenant_flesh_print_line = f"How much Revenant Flesh you need: {can_craft_count * 128}"

        if can_craft_count * 32 > 71680:
            enchanted_string_print_line = f"""Enchanted String 71680x Orders: {trunc(can_craft_count * 32 / 71680)}
Enchanted String Rest Order: {round(((can_craft_count * 32 / 71680) - trunc(can_craft_count * 32 / 71680)) * 71680)}"""

        else:
            enchanted_string_print_line = f"How much Enchanted String you need: {can_craft_count * 32}"

        if balance < revenant_viscera_craft_price:
            print("\u001b[31mYou dont have enough money!\033[0m\n")

        else:
            print(f"""\nEstimated profit: {estimated_profit}
Money you have at the end: {int(balance + estimated_profit)}
How much you can craft: {can_craft_count}
{revenant_flesh_print_line}
{enchanted_string_print_line}\n""")

def german():
    while True:
        balance = float(input("Wie viel Geld hast du? "))
        revenant_flesh_price = float(load(urlopen("https://api.hypixel.net/skyblock/bazaar"))["products"]["REVENANT_FLESH"]["sell_summary"][0]["pricePerUnit"]) + 0.1
        enchanted_string_price = float(load(urlopen("https://api.hypixel.net/skyblock/bazaar"))["products"]["ENCHANTED_STRING"]["sell_summary"][0]["pricePerUnit"]) + 0.1
        revenant_viscera_sell_price = float(load(urlopen("https://api.hypixel.net/skyblock/bazaar"))["products"]["REVENANT_VISCERA"]["buy_summary"][0]["pricePerUnit"])
        revenant_viscera_craft_price = (revenant_flesh_price * 128) + (enchanted_string_price * 32)
        can_craft_count = int(balance / revenant_viscera_craft_price)
        estimated_profit = int(can_craft_count * (revenant_viscera_sell_price - revenant_viscera_craft_price))

        if can_craft_count * 128 > 71680:
            revenant_flesh_print_line = f"""Revenant Flesh 71680x Order: {trunc(can_craft_count * 128 / 71680)}
Revenant Flesh Rest Order: {round(((can_craft_count * 128 / 71680) - trunc(can_craft_count * 128 / 71680)) * 71680)}"""

        else:
            revenant_flesh_print_line = f"Wie viel Revenant Flesh du brauchst: {can_craft_count * 128}"

        if can_craft_count * 32 > 71680:
            enchanted_string_print_line = f"""Enchanted String 71680x Order: {trunc(can_craft_count * 32 / 71680)}
Enchanted String Rest Order: {round(((can_craft_count * 32 / 71680) - trunc(can_craft_count * 32 / 71680)) * 71680)}"""

        else:
            enchanted_string_print_line = f"Wie viel Enchanted String du brauchst: {can_craft_count * 32}"

        if balance < revenant_viscera_craft_price:
            print("\u001b[31mDu hast nicht genug Geld!\033[0m\n")

        else:
            print(f"""\nGeschätzter Profit: {estimated_profit}
Wie viel Geld du am Ende hast: {int(balance + estimated_profit)}
Wie viel du craften kannst: {can_craft_count}
{revenant_flesh_print_line}
{enchanted_string_print_line}\n""")

while True:
    lang = input('What language do you want to use? English (type "en") or German (type "de")? ').lower()
    
    if lang == "en":
        english()

    elif lang == "de":
        german()
    
    else:
        print("\u001b[31mNo, try again.\033[0m\n")