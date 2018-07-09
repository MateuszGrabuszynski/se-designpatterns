"""@package docstring
Build me a muffin please.
"""
import abc


class Muffin():
    """Complex muffin construction."""
    def __init__(self):
        self.mainTaste = ""
        self.toppingTaste = ""
        self.toppingType = ""
        self.doughType = ""

    def set_main_taste(self, mt):
        """Sets muffin's main taste (main ingredient/s)."""
        self.mainTaste = mt

    def set_topping_taste(self, tta):
        """Sets topping's taste."""
        self.toppingTaste = tta

    def set_topping_type(self, tty):
        """Sets topping type."""
        self.toppingType = tty

    def set_dough_type(self, dt):
        """Sets dough type."""
        self.doughType = dt


class Confectioner(metaclass=abc.ABCMeta):
    """Builds every part of muffin you want to eat. ;)"""
    def __init__(self):
        self.muffin = Muffin()
        self.preheat_oven()
        self.grease_pan()
        self.mix_ingredients()
        self.put_mixture_into_muffin_cups()
        self.bake()
        self.cool()
        self.refrigerate()
        self.glaze()

    @abc.abstractmethod
    def preheat_oven(self):
        """Used to preheat oven to specific temp."""
        pass

    @abc.abstractmethod
    def grease_pan(self):
        """If the pen needs to be greased beforehead, use this."""
        pass

    @abc.abstractmethod
    def mix_ingredients(self):
        """Mixes 'em all together."""
        pass

    @abc.abstractmethod
    def put_mixture_into_muffin_cups(self):
        """Pours the mix into muffin cups."""
        pass

    @abc.abstractmethod
    def bake(self):
        """Oven time."""
        pass

    @abc.abstractmethod
    def cool(self):
        """Don't eat 'em too hot please!"""
        pass

    @abc.abstractmethod
    def refrigerate(self):
        """Some of them does need special care"""
        pass

    @abc.abstractmethod
    def glaze(self):
        """And some topping"""
        pass


class StrawberryMuffinsConfectioner(Confectioner):
    """An assembler, constructor and provider of strawberry heaven at the same time."""
    def preheat_oven(self):
        print('Oven set to 190 deg Celsius.')

    def grease_pan(self):
        print('Pan for 6 muffins greased.')

    def mix_ingredients(self):
        self.muffin.set_main_taste("Strawberry")
        print('Combined 1/4 cup of canola oil, 1/2 cup of milk and 1 egg in a bowl. Beaten them lightly.'
              'Mixed 1 and 3/4 cups of all-purpose flour, 1/2 teaspoon of salt, 2 teaspoons of baking powder'
              'and 1/2 cup of sugar in other bowl. Tossed in chopped strawberries. Poured milk mixture...')

    def put_mixture_into_muffin_cups(self):
        print('Mixed all together and put into muffin cups.')

    def bake(self):
        self.muffin.set_dough_type("Crusty outside, soft inside.")
        print('Baked for 25 minutes.')

    def cool(self):
        print("Cooled 10 min.")

    def glaze(self):
        self.muffin.set_topping_taste("None")
        self.muffin.set_topping_type("Invisible")

    def refrigerate(self):
        pass


class BananaMangoMuffinsConfectioner(Confectioner):
    """An assembler, constructor and provider of banana&mango heaven at the same time."""
    def preheat_oven(self):
        print('Oven set to 175 deg Celsius.')

    def grease_pan(self):
        print('Pan for 18 muffins greased.')

    def mix_ingredients(self):
        self.muffin.set_main_taste("Mango and banana")
        print('Blended 1 mango, 3 bananas, 2/3 cup brown sugar, juice of 1/2 lime until smooth. '
              'Whisked 2 cups of all-purpose flour, 1 teaspoon of baking soda, baking powder and cinnamon,'
              ' 1/4 teaspoon of nutmeg and 1/8 of allspice together in a bowl.'
              'Mixed 1/2 cup of room-temp butter, 3 large eggs and mango-banana'
              'mixture into flour mixture until combined.')

    def put_mixture_into_muffin_cups(self):
        print('Mixed all together and put into muffin cups.')

    def bake(self):
        self.muffin.set_dough_type("Soft")
        print('Baked for around 27 minutes.')

    def cool(self):
        print("Cooled 10 min inside pans.")

    def glaze(self):
        self.muffin.set_topping_type("Thick glaze")
        self.muffin.set_topping_taste("Lime")
        print('Thickly glazed with whisked confectioners\' sugar and teaspoon of lime juice onto cooled muffins.')

    def refrigerate(self):
        pass


class Waiter():
    """Directs a construction of 6 muffins being held by the Builder interface."""

    def __init__(self):
        self._builder = None

    def construct_muffin(self, builder):
        """Constructs the whole muffin thing"""
        self._builder = builder
        self._builder.preheat_oven()
        self._builder.grease_pan()
        self._builder.mix_ingredients()
        self._builder.put_mixture_into_muffin_cups()
        self._builder.bake()
        self._builder.cool()
        self._builder.refrigerate()


if __name__ == "__main__":
    waiter = Waiter()

    strawberryMuffin = StrawberryMuffinsConfectioner()
    waiter.construct_muffin(strawberryMuffin)

    myMuffin = strawberryMuffin.muffin
    mainTaste = myMuffin.mainTaste

    print("First muffin:" + mainTaste)

    mangoMuffin = BananaMangoMuffinsConfectioner()
    waiter.construct_muffin(mangoMuffin)

    my2ndMuffin = mangoMuffin.muffin
    mainTasteThe2nd = my2ndMuffin.mainTaste

    print("Second muffin:" + mainTasteThe2nd)