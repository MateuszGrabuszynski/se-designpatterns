"""@package docstring
Allows to dynamically attach additional properties to buttons.
"""
import abc


class Button(metaclass=abc.ABCMeta):
    """
    Interface for objects with additional properties.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abc.abstractmethod
    def draw(self):
        """Draws the button."""
        pass


class BorderType(Button, metaclass=abc.ABCMeta):
    """
    Add border type or remove it.
    """

    def __init__(self, button):
        self._button = button

    @abc.abstractmethod
    def draw(self):
        """Operation for drawing the button with specific border type"""
        print('  BorderType')
        return 'BorderType'


class BorderColor(BorderType):
    """
    Allows to add the color of border.
    """

    def draw(self):
        """Operation for drawing the border of the button with specific color."""
        self._button.draw()
        print('  BorderColor')
        return 'BorderColor'


class BorderThickness(BorderType):
    """
    Allows to add thickness of the border.
    """

    def draw(self):
        """Operation for drawing the button with specific border thickness."""
        self._button.draw()
        print('  BorderThickness')
        return 'BorderThickness'


class SendButton(Button):
    """
    Object, that additional properties can be attached to.
    """

    def draw(self):
        """Operation for drawing the button."""
        print('SendButton at '+str(self.x)+','+str(self.y))
        return 'SendButton at '+str(self.x)+','+str(self.y)


if __name__ == "__main__":
    # version1
    # sendBtn = SendButton()
    # borderColor = BorderColor(sendBtn)
    # borderThickness = BorderThickness(borderColor)
    #
    # borderThickness.draw()

    # version2
    sendBtn2 = BorderThickness(BorderThickness(BorderColor(SendButton(10,20))))
    x = sendBtn2.draw()
    print(x)