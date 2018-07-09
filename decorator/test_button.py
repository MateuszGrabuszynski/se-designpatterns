from unittest import TestCase


class TestButton(TestCase):
    def test_draw(self):
        from decorator import SendButton, BorderColor, BorderThickness

        print('test1:')
        sendBtn1 = SendButton(10, 20)
        self.assertEqual(sendBtn1.draw(), 'SendButton at 10,20')

        print('\ntest2:')
        sendBtn2 = BorderColor(sendBtn1)
        self.assertEqual(sendBtn2.draw(), 'BorderColor')

        print('\ntest3:')
        sendBtn3 = BorderThickness(sendBtn2)
        self.assertEqual(sendBtn3.draw(), 'BorderThickness')

        print('\ntest4:')
        sendBtn4 = BorderColor(sendBtn2)
        self.assertEqual(sendBtn4.draw(), 'BorderColor')

        print('\ntest5:')
        sendBtn5 = BorderColor(sendBtn3)
        self.assertEqual(sendBtn5.draw(), 'BorderColor')

        print('\ntest6:')
        sendBtn6 = BorderThickness(sendBtn3)
        self.assertEqual(sendBtn6.draw(), 'BorderThickness')
