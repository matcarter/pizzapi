

class DataManager:
    """
    Used to manage the stored data
    """

    @staticmethod
    def menu():
        data_strings = ["Manage Coupons", "Manage Customers", "Manage Orders", "Quit"]

        while True:
            print("\n- Saved Data Manager -")

            for i, action in enumerate(data_strings):
                print("\t" + str(i + 1) + ". " + action)

            index = int(input("Enter the # of the action: ").strip())

            while index < 1 or index > len(data_strings):
                print("Please enter a value between {} and {}".format(1, len(data_strings)))
                index = int(input("Enter the # of the action: ").strip())

            index -= 1

            if data_strings[index] == "Manage Coupons":
                DataManager.manage_coupons()
            elif data_strings[index] == "Manage Customers":
                DataManager.manage_customers()
            elif data_strings[index] == "Manage Orders":
                DataManager.manage_orders()
            else:
                return

    @staticmethod
    def manage_coupons():
        print("\n- Coupon Manager -")
        return

    @staticmethod
    def manage_customers():
        print("\n- Customer Manager -")
        return

    @staticmethod
    def manage_orders():
        print("\n- Order Manager -")
        return


class CouponManager:
    """
    Used to manage coupons
    """

    @staticmethod
    def add_coupon():
        print("\n- Add Coupon -")
        return

    @staticmethod
    def remove_coupon():
        print("\n- Remove Coupon -")
        return

    @staticmethod
    def view_coupons():
        print("\n- View Coupons -")
        return


class CustomerManager:
    """
    Used to manage coupons
    """

    @staticmethod
    def add_customer():
        print("\n- Add Coupon -")
        return

    @staticmethod
    def remove_customer():
        print("\n- Remove Coupon -")
        return

    @staticmethod
    def view_customers():
        print("\n- View Coupons -")
        return


class OrderManager:
    """
    Used to manage coupons
    """

    @staticmethod
    def add_order():
        print("\n- Add Coupon -")
        return

    @staticmethod
    def remove_order():
        print("\n- Remove Coupon -")
        return

    @staticmethod
    def view_orders():
        print("\n- View Coupons -")
        return
