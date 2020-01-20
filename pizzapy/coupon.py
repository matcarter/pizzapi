import json


class Coupon(object):
    """Loose representation of a coupon - no logic. 

    This is a coupon - you can add it to an Order (order.add_item) and,
    if it fits, get some money off your purchase. I think. 

    This is another thing that's worth exploring - there are some sweet 
    coupons that would be awful without the coupon. 
    """
    def __init__(self, code, quantity=1):
        self.code = code
        self.quantity = quantity
        self.id = 1
        self.is_new = True

    def save(self, filename="data/coupons/coupon1.json"):
        """
        saves the current coupon to a .json file for loading later
        """
        if not filename.startswith("data/coupons"):
            filename = "data/coupons/" + filename
        json_dict = {"code": self.code,
                     "quantity": self.quantity}

        with open(filename, "w") as f:
            json.dump(json_dict, f)

    @staticmethod
    def load(filename):
        """
        load and return a new coupon object from a json file
        """
        with open(filename, "r") as f:
            data = json.load(f)

            coupon = Coupon(data["code"],
                            data["quantity"])
        return coupon

    def __repr__(self):
        return "Code: {}\nQuantity: {}".format(
            self.code,
            self.quantity,
        )