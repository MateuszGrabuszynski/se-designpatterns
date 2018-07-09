from unittest import TestCase


class TestReceiptPrototype(TestCase):
    def test_all(self):
        # tests all at once
        from prototype import ReceiptPrototype
        prototype = ReceiptPrototype()
        receipts = []
        import copy
        receipts.append(prototype.copy_me())

        receipts[0].add_product('Butter', 3, 3.45, 'a')
        receipts[0].add_product('Milk', 2, 2.00, 'b')

        self.assertEqual(receipts[0].return_receipt(1344),
                         "------\nLidl sp. z o.o. sp. k.\nPilsudskiego 116\n61-246 Poznan\nNIP: 781-18-97-358\n\nPARAGON FISKALNY\nnr wydr.1344\n\nButter\t(a)\t3 * 4.24\t=\t12.72\nMilk\t(b)\t2 * 2.16\t=\t4.32\n\nPTU A 23%:\t2.38\nPTU B 8%:\t0.32\nPTU C 5%:	0.0\nBEZ PTU:\t14.35\nSUMA PLN:\t17.05\n\n---\nDziękujemy za zakupy w Lidl!\nPobierz: www.lidl.pl/aplikacja\nAktualna oferta na lidl.pl\n...\n------")

        receipts.append(prototype.copy_me())
        receipts[1].add_product('Olives', 2, 2.25, 'b')
        self.assertEqual(len(receipts[0].products), 2)
        self.assertEqual(len(receipts[1].products), 1)

    def test_sum_all(self):
        from prototype import ReceiptPrototype
        prototype = ReceiptPrototype()
        receipts = []
        import copy
        receipts.append(prototype.copy_me())
        receipts[0].add_product('Bread', 2, 2.00, 'a')
        receipts[0].add_product('Milk', 2, 2.00, 'b')
        receipts[0].add_product('Tissues', 2, 2.00, 'c')

        receipts[0].sum_all()
        self.assertEqual(receipts[0].sum, 12.00)
        self.assertEqual(receipts[0].sumPTUA, 0.92)
        self.assertEqual(receipts[0].sumPTUB, 0.32)
        self.assertEqual(receipts[0].sumPTUC, 0.20)
        self.assertEqual(receipts[0].sumWithPTUs, 13.44)

    def test_add_product(self):
        from prototype import ReceiptPrototype
        prototype = ReceiptPrototype()
        receipt = prototype.copy_me()
        self.assertEqual(len(receipt.products), 0)

        receipt.add_product('Flour', 3, 11.00, 'b')
        self.assertEqual(len(receipt.products), 1)
        self.assertEqual(receipt.products[0]['name'], 'Flour')
        self.assertEqual(receipt.products[0]['amount'], 3)
        self.assertEqual(receipt.products[0]['price'], 11.00)
        self.assertEqual(receipt.products[0]['ptu'], 'b')
