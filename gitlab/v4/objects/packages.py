from gitlab.base import RESTManager, RESTObject
from gitlab.mixins import DeleteMixin, GetMixin, ListMixin, ObjectDeleteMixin


__all__ = [
    "GroupPackage",
    "GroupPackageManager",
    "ProjectPackage",
    "ProjectPackageManager",
]


class GroupPackage(RESTObject):
    pass


class GroupPackageManager(ListMixin, RESTManager):
    _path = "/groups/%(group_id)s/packages"
    _obj_cls = GroupPackage
    _from_parent_attrs = {"group_id": "id"}
    _list_filters = (
        "exclude_subgroups",
        "order_by",
        "sort",
        "package_type",
        "package_name",
    )


class ProjectPackage(ObjectDeleteMixin, RESTObject):
    pass


class ProjectPackageManager(ListMixin, GetMixin, DeleteMixin, RESTManager):
    _path = "/projects/%(project_id)s/packages"
    _obj_cls = ProjectPackage
    _from_parent_attrs = {"project_id": "id"}
    _list_filters = (
        "order_by",
        "sort",
        "package_type",
        "package_name",
    )
