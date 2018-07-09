"""@package docstring
Observer example.
"""
import abc


class Auction:
    """Knows its bidders and notifies them when he accepts the bid."""
    def __init__(self):
        self._bidders = set()
        self._auction_state = None

    def attach(self, bidder):
        bidder._subject = self
        self._bidders.add(bidder)

    def detach(self, bidder):
        bidder._subject = self
        self._bidders.discard(bidder)

    def _notify(self):
        for bidder in self._bidders:
            bidder.update(self._auction_state)

    @property
    def auction_state(self):
        return self._auction_state

    @auction_state.setter
    def auction_state(self, bid):
        self._auction_state = bid
        self._notify()


class Bidder(metaclass=abc.ABCMeta):
    """Bidder class."""
    def __init__(self):
        self._auction = None
        self._bidder_state = None

    @abc.abstractmethod
    def update(self, bid):
        pass


class CrazyBidder(Bidder):
    def update(self, bid):
        self._bidder_state = bid


class VeryCrazyBidder(Bidder):
    def update(self, bid):
        self._bidder_state = bid


if __name__ == "__main__":
    # auction creation
    auction = Auction()

    # adding bidders
    crazyGuy1996 = CrazyBidder()
    auction.attach(crazyGuy1996)
    savageMan1 = VeryCrazyBidder()
    auction.attach(savageMan1)

    for x in auction._bidders:
        break
    print(isinstance(x, VeryCrazyBidder))
    print(x)

    # changing auction state (auto-notify)
    auction.auction_state = 2029

    # printing results (bidders auction state)
    print(savageMan1._bidder_state)
    print(crazyGuy1996._bidder_state)

    # detach 1 user
    auction.detach(crazyGuy1996)

    # changing auction state (auto-notify)
    auction.auction_state = 5555

    # printing results (bidders auction state)
    print(savageMan1._bidder_state)
    print(crazyGuy1996._bidder_state)