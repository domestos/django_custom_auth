"""This mixin we can use only with class with has get_object (generic.classes) """

from django.http import Http404
class ProfilePermissionsMixin:
    def has_permissions(self):
        print(self.get_object() )
        print(self.request.user )
        return self.get_object() == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)