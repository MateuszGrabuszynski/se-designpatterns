from unittest import TestCase


class TestAuction(TestCase):
    def test_all(self):
        """ Tests attach, detach and _notify."""
        # auction creation
        from observer import Auction
        auction = Auction()

        # adding bidders
        from observer import CrazyBidder
        crazyGuy1996 = CrazyBidder()
        auction.attach(crazyGuy1996)

        # check attach function
        for x in auction._bidders:
            break
        self.assertTrue(isinstance(x, CrazyBidder))
        self.assertEqual(len(auction._bidders), 1)

        # add another bidder (mainly for broadcasting and detachment check)
        from observer import VeryCrazyBidder
        savageMan1 = VeryCrazyBidder()
        auction.attach(savageMan1)

        # check attach once more
        self.assertEqual(len(auction._bidders), 2)

        # check if both bidders notified (broadcasting check)
        auction.auction_state = 2029
        self.assertEqual(crazyGuy1996._bidder_state, 2029)
        self.assertEqual(savageMan1._bidder_state, 2029)

        # check detach function
        auction.detach(savageMan1)
        self.assertEqual(len(auction._bidders), 1)

        # check if only one of two bidders notified (broadcasting check)
        auction.auction_state = 1111
        self.assertEqual(crazyGuy1996._bidder_state, 1111)
        self.assertNotEqual(savageMan1._bidder_state, 1111)
