from django.core.exceptions import PermissionDenied


class AnyGroupRequiredMixin:
    required_groups = []

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            raise PermissionDenied
        if not request.user.groups.exists():
            raise PermissionDenied

        group_names = [g.name for g in request.user.groups.all()]
        result = set(group_names).intersection(self.required_groups)
        if self.required_groups and not result:
            return PermissionDenied

        return super().dispatch(request, *args, **kwargs)