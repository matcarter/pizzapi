# fork from https://github.com/Magicjarvis/pizzapi
from pizzapy import ConsoleInput, DataManager, StoreLocator, Customer, Address


def main():
    general_actions = ["Manage Saved Data (Coupons, Customers, Orders, etc.)", "Place an Order",
                       "View nearby Stores", "View the Menu", "Quit"]
    general_methods = [DataManager.menu, place_order, view_stores, view_menu, quit]

    print("####################")
    print(" Welcome to Dominos ")
    print("####################")

    while True:
        index = menu(general_actions)
        general_methods[index]()

    # customer = ConsoleInput.get_customer()
    # customer.save(customer.first_name + " " + customer.last_name)
    # show_stores(customer, 5)
    # card = ConsoleInput.get_credit_card()


def menu(available_actions) -> int:
    print("\n- Menu -")

    for i, action in enumerate(available_actions):
        print("\t" + str(i + 1) + ". " + action)

    index = int(input("Enter the # of the action: ").strip())

    while index < 1 or index > len(available_actions):
        print("Please enter a value between {} and {}".format(1, len(available_actions)))
        index = int(input("Enter the # of the action: ").strip())

    return index - 1


def place_order():
    return


def view_stores():
    print("\n- Store Locator -")

    print("\tPlease type your ADDRESS using the following form.")
    print("\tHOUSE #, Full Street Name, City, State/Province, ZIP/Postal Code")
    print("\tEXAMPLE: 700 Pennsylvania Avenue NW, Washington, DC, 20408")

    ret_address = ConsoleInput.get_valid_input("ADDRESS: ", ConsoleInput.validate_address)
    address = Address(*ret_address.split(','))

    print("\n- CLOSEST STORES -")
    local_stores = StoreLocator.nearby_stores(address)
    for i, store in enumerate(local_stores[:5]):
        print(str(i + 1) + ".")
        print(store)
        print()

    return


def view_menu():
    print("\n- Menu Viewer -")

    print("\tPlease type your ADDRESS using the following form.")
    print("\tHOUSE #, Full Street Name, City, State/Province, ZIP/Postal Code")
    print("\tEXAMPLE: 700 Pennsylvania Avenue NW, Washington, DC, 20408")

    ret_address = ConsoleInput.get_valid_input("ADDRESS: ", ConsoleInput.validate_address)
    address = Address(*ret_address.split(','))

    closest_store = StoreLocator.nearby_stores(address)[0]

    menu = closest_store.get_menu()

    print(menu)

    return


if __name__ == "__main__":
    main()
