from gitlab.base import RESTManager, RESTObject
from gitlab.mixins import CRUDMixin, ObjectDeleteMixin, SaveMixin


__all__ = [
    "BroadcastMessage",
    "BroadcastMessageManager",
]


class BroadcastMessage(SaveMixin, ObjectDeleteMixin, RESTObject):
    pass


class BroadcastMessageManager(CRUDMixin, RESTManager):
    _path = "/broadcast_messages"
    _obj_cls = BroadcastMessage

    _create_attrs = (("message",), ("starts_at", "ends_at", "color", "font"))
    _update_attrs = (tuple(), ("message", "starts_at", "ends_at", "color", "font"))
