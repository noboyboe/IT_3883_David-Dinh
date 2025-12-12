statement = input("State an amount of money: ")

def remove():
    item = statement.split()
    for x in item:
        if x == "and":
            item.remove("and")
    return item
#remove() splits the statement into a list and removes "and" to make it easier to convert.

def convert(item):
    final_total = 0
    i = 0

    while i < len(item):
        quantity = int(item[i])
        coin = item[i+1]

        if coin in ["penny", "pennies"]:
            dollar = 0.01
        elif coin in ["nickel", "nickels"]:
            dollar = 0.05
        elif coin in ["dime", "dimes"]:
            dollar = 0.10
        elif coin in ["quarter", "quarters"]:
            dollar = 0.25

        final_total += quantity * dollar
        i += 2

    print(f"You have: ${final_total:.2f}")

clean_list = remove()
convert(clean_list)

