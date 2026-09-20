# add inital vars
bakery_name = None
lvl = 1
days = 0
menu = ["Bread"]
Money = 100
income = 0
expenses = 0
def main():
    print("Welcome to Bakery!")
    print("\n")
    start = input("Start game?(y/n) ")
    if start == "y":
        name_bakery(input("What is your bakery's name? "))
        print("\n")
        view_stats()

def name_bakery(nim):
    global bakery_name
    bakery_name = nim
def view_stats():
    print(f"Bakery Name: {bakery_name}")
    print(f"Level: {lvl}")
    print(f"Days: {days}")
    print(f"Menu: {menu}")
    print("Money" + calc_money(Money, income , expenses))
    print(calc_profit(income, expenses))

def calc_money(mon, inc, exp):
    finmon = (mon + inc) - exp
    return "$" + str(finmon)
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
# add main func:
main()
