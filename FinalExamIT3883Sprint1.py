statement = input("State an amount of money: ")
print("Enter 'STOP' if you wish to end the program.")

def remove():
    item = statement.split()
    for x in item:
        if x == "and":
            item.remove("and")
    return item
#remove() splits the statement into a list and removes "and" to make it easier to convert.
def convert(item):
    conversion = []
    for x in item[0:2]:
        conversion.append(x)
#Items are appended into the "conversion" list as pairs.
    quantity = int(conversion[0])
    conversion.remove(conversion[0])
#The first number is the quantity and is removed from the "conversion" list for later values to be appended.
    for x in conversion:
        if x == "penny" or "pennies":
            x = 0.01
        elif x == "nickel" or "nickels":
            x = 0.05
        elif x == "dime" or "dimes":
            x = 0.10
        elif x == "quarter" or "quarters":
            x = 0.25
#This for loop identifies the keywords in a statement and converts it into values.
        dollar = x
        conversion.remove(conversion[0])
#The second number is the dollar amount and is removed from the "conversion" list for later values to be appended.
        total = quantity * dollar
        print(f"You have: ${total:.2f}")

    print(conversion)

clean_list = remove()

convert(clean_list)
