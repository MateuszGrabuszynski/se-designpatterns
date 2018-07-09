"""@package docstring
Prototype example - receipt used in cash machines.
"""

import copy

PTUA = 0.23
PTUB = 0.08
PTUC = 0.05


class ReceiptPrototype:
    """Prototype of the receipt class."""

    def __init__(self):
        self.shopFullName = "Lidl sp. z o.o. sp. k."
        self.shopAddress = "Pilsudskiego 116\n61-246 Poznan"
        self.nipNumber = "781-18-97-358"
        self.header = "PARAGON FISKALNY"
        self.additionalInfo = "Dziękujemy za zakupy w Lidl!\nPobierz: www.lidl.pl/aplikacja\nAktualna oferta na lidl.pl\n..."
        self.receiptNumber = None
        self.receiptNumberMessage = "nr wydr. "

        self.products = list()

        self.sum = 0.0
        self.sumPTUA = 0.0
        self.sumPTUB = 0.0
        self.sumPTUC = 0.0
        self.sumWithPTUs = 0.0

    def sum_dall(self):
        """Method summing up all elements of the receipt at the end of transaction"""
        for product in self.products:
            productPrice = float(product['price'])*int(product['amount'])
            self.sum += round(productPrice,2) # adding prices without taxes
            # adding taxes values
            if product['ptu'] == 'a':
                self.sumPTUA += round(PTUA*productPrice,2)
            elif product['ptu'] == 'b':
                self.sumPTUB += round(PTUB*productPrice,2)
            elif product['ptu'] == 'c':
                self.sumPTUC += round(PTUC*productPrice,2)
            else:
                print('Unknown PTU type!')

        # sum with taxes
        self.sumWithPTUs = self.sum + self.sumPTUA + self.sumPTUB + self.sumPTUC

    def add_product(self, name, amount, price, ptu):
        """Adds product to receipt"""
        self.products.append({'name': name, 'amount': amount, 'price': float(price), "ptu": ptu})

    def stringify_products(self):
        """Returns one big string with all products. Needed for printer."""
        result = ''

        for product in self.products:
            result += product['name'] + "\t(" + product['ptu'] + ")\t" + str(product['amount']) + " * "
            if product['ptu'] == 'a':
                fullPrice = float(product['price']) + round((float(product['price']) * PTUA),2)
            elif product['ptu'] == 'b':
                fullPrice = float(product['price']) + round((float(product['price']) * PTUB),2)
            elif product['ptu'] == 'c':
                fullPrice = float(product['price']) + round((float(product['price']) * PTUC),2)
            result += str(fullPrice) + "\t=\t" + str(fullPrice * float(product['amount'])) + "\n"

        return result

    def return_receipt(self, receiptNumber):
        """Returns string to be sent to printer."""
        self.receiptNumber = receiptNumber
        self.sum_all()
        allProductsString = self.stringify_products()

        return "------\n" + self.shopFullName + "\n" + self.shopAddress + "\nNIP: " + self.nipNumber + "\n\n" +\
               self.header + "\n" + "nr wydr." + str(self.receiptNumber) + "\n\n" +\
               allProductsString +\
               "\nPTU A " + str(int(PTUA * 100)) + "%:\t" + str(self.sumPTUA) + \
               "\nPTU B " + str(int(PTUB * 100)) + "%:\t" + str(self.sumPTUB) + \
               "\nPTU C " + str(int(PTUC * 100)) + "%:\t" + str(self.sumPTUC) + \
               "\nBEZ PTU:\t" + str(self.sum) + \
               "\nSUMA PLN:\t" + str(round(self.sum + self.sumPTUA + self.sumPTUB + self.sumPTUC,2)) + \
               "\n\n---\n" + self.additionalInfo + "\n------"

    def copy_me(self):
        return copy.deepcopy(self)


if __name__ == "__main__":
    """Main function of the prototype example"""
    prototype = ReceiptPrototype()
    receipts = []
    receipts.append(prototype.copy_me())

    receipts[0].add_product('Butter', 3, 3.45, 'a')
    receipts[0].add_product('Milk', 2, 2.00, 'b')

    print(receipts[0].return_receipt(1344))

    receipts.append(prototype.copy_me())
    receipts[1].add_product('Bread', 2, 2.00, 'a')
    receipts[1].add_product('Milk', 2, 2.00, 'b')
    receipts[1].add_product('Tissues', 2, 2.00, 'c')

    print(receipts[0].products[0])
    #print(receipts[0].return_receipt(555))