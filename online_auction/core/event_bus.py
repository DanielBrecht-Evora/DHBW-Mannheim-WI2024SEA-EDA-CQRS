from collections import defaultdict
from typing import Callable, Type
from .base_event import BaseEvent


class EventBus:
    """
    Zentraler Event Bus - das Herzstück der EDA.

    Consumers (Handler) registrieren sich für bestimmte Event-Typen.
    Wenn ein Producer ein Event publiziert, benachrichtigt der Bus
    automatisch alle registrierten Consumer.
    """

    def __init__(self):
        # Speichert: Event-Typ → Liste von Handler-Funktionen
        self._subscribers: dict[Type[BaseEvent], list[Callable]] = defaultdict(list)

    def subscribe(self, event_type: Type[BaseEvent], handler: Callable) -> None:
        """Consumer registriert sich für einen Event-Typ."""
        self._subscribers[event_type].append(handler)

    def publish(self, event: BaseEvent) -> None:
        """Producer veröffentlicht ein Event an alle Consumer."""
        handlers = self._subscribers.get(type(event), [])
        for handler in handlers:
            handler(event)
