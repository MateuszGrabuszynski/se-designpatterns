from unittest import TestCase


class TestWaiter(TestCase):
    def test_construct_muffin_strawberry(self):
        from builder import Waiter
        waiter = Waiter()
        from builder import StrawberryMuffinsConfectioner
        strawberry_muffin = StrawberryMuffinsConfectioner()
        waiter.construct_muffin(strawberry_muffin)

        my_muffin = strawberry_muffin.muffin

        self.assertEqual(my_muffin.mainTaste, "Strawberry")
        self.assertEqual(my_muffin.toppingTaste, "None")
        self.assertEqual(my_muffin.toppingType, "Invisible")
        self.assertEqual(my_muffin.doughType, "Crusty outside, soft inside.")

    def test_construct_muffin_bananamango(self):
        from builder import Waiter
        waiter = Waiter()
        from builder import BananaMangoMuffinsConfectioner
        bananamango_muffin = BananaMangoMuffinsConfectioner()
        waiter.construct_muffin(bananamango_muffin)

        my_muffin = bananamango_muffin.muffin

        self.assertEqual(my_muffin.mainTaste, "Mango and banana")
        self.assertEqual(my_muffin.toppingTaste, "Lime")
        self.assertEqual(my_muffin.toppingType, "Thick glaze")
        self.assertEqual(my_muffin.doughType, "Soft")