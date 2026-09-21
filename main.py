import random
import time
import os
import subprocess
# add inital vars
bakery_name = None
lvl = 1
days = 0
menu = ["Bread"]
baking_prices = [100]
Money = 100
income = 0
expenses = 0
actions  = ["bake", "advertize"]
batch_size = [10]
baking_idx = 0
inv = []
inv_amount = []
inv_idx = 0
avg_costomers = 11.5
def main():
    print("Welcome to Bakery!")
    print("\n")
    start = input("Start game?(y/n) ")
    if start == "y":
        name_bakery(input("What is your bakery's name? "))
        print("\n")
        view_stats()
        time.sleep(2.5)
        clear_screen()
        increment_day()
        process_actions()
    elif start == "n":
        print("Exiting game...")
        time.sleep(1)
        exit()
        

def name_bakery(nim):
    global bakery_name
    bakery_name = nim
def view_stats():
    calc_money(Money, income , expenses)
    print(f"Bakery Name: {bakery_name}")
    print(f"Level: {lvl}")
    print(f"Days: {days}")
    print(f"Menu: {menu}")
    print(f"Money: {Money}")
    print(calc_profit(income, expenses))

def calc_money(mon, inc, exp):
    global Money
    finmon = (mon + inc) - exp
    Money = finmon
def calc_profit(inc, exp):
    calres = inc - exp
    if calres > 0:
        return str(calres) + " money made."
    elif calres < 0:
        return str(neg(calres)) + " money lost."
    else:
        return "You didn't make any money today."
def neg(val):
    return val - val * 2

def increment_day():
    global days
    days += 1
    print("Entering Day " + str(days) + ".")
def process_actions():
    global actions
    global money
    global expenses
    global menu
    global baking_prices
    global baking_idx
    global batch_size
    global inv
    global inv_amount
    global avg_costomers
    curentaction = input("What do you want to do?\n" + str(actions) + "?\n")
    if curentaction in actions:
        if curentaction == "bake":
            baked_good = input("What do want to bake? " + str(menu))
            if baked_good in menu:
                baking_idx = menu.index(baked_good)
                print("Baking " + baked_good)
                expenses += baking_prices[baking_idx]
                inv.append(menu[baking_idx])
                inv_amount.append(batch_size[baking_idx])
        elif curentaction == "advertize":
            avg_costomers += random.uniform(0.5, 5)
    else:
        print("Invalid action. Try again.")
        process_actions()

def clear_screen():
    if os.name == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

# add main func:
main()
