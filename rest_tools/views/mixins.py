from rest_framework import views


class ParentViewSetMixin(views.APIView):
    parent_lookup_url_kwarg = None
    parent_field = None

    def __init_subclass__(cls, **kwargs):
        assert getattr(cls, 'parent_lookup_url_kwarg', None), "You have to set `parent_lookup_url_kwarg`"
        assert getattr(cls, 'parent_field', None), "You have to set `parent_lookup_url_kwarg`"

    def get_queryset(self):
        return super().get_queryset().filter(**{f'{self.parent_field}__pk': self.kwargs[self.parent_lookup_url_kwarg]})

    # def check_permissions(self, request):
    #     if self.inherit_permissions:
    #         return
