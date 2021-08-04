from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(),
                                     self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect(reverse_lazy('home:forbidden')) #نحط الرابط اللي نبغاه يرجع له اذا مو مسجل أو ما عنده الصلاحية
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)