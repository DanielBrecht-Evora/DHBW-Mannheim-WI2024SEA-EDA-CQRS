from dataclasses import dataclass
from ..core.base_event import BaseEvent


@dataclass
class BidPlaced(BaseEvent):
    """Event: Ein neues Gebot wurde abgegeben."""
    auction_id: str = ""
    bidder_name: str = ""
    amount: float = 0.0
