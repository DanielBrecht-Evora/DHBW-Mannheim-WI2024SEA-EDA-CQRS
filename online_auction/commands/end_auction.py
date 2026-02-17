from dataclasses import dataclass
from ..core.base_command import BaseCommand


@dataclass
class EndAuction(BaseCommand):
    """Command: Beende eine laufende Auktion."""
    auction_id: str
