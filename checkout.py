class Checkout:
    def __init__(self):
        self.customerName = ""
        self.discountPercent = 0

    def calculate_total(self, subtotal, taxRate):
        finalPrice = subtotal + (subtotal * taxRate)
        return finalPrice
