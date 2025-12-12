statement = input("State an amount of money: ")
#Asks the user to input a statement
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
#Continues to loop until there are no more items in the list to take values from.
        if coin in ["penny", "pennies"]:
            dollar = 0.01
        elif coin in ["nickel", "nickels"]:
            dollar = 0.05
        elif coin in ["dime", "dimes"]:
            dollar = 0.10
        elif coin in ["quarter", "quarters"]:
            dollar = 0.25
#Looks for keywords in the statement and changes the values of "quantity" and "dollar" to multiply and add on to the "final_total"
        final_total += quantity * dollar
        i += 2
# i += 2 continues the loop by moving to the next pair in the list.
    print(f"You have: ${final_total:.2f}")

clean_list = remove()
convert(clean_list)


