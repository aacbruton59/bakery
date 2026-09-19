# add inital vars
bakery_name = None
lvl = 1
days = 0
menu = ["Bread"]
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



# add main func:
main()
