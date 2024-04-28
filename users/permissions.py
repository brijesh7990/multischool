from django.contrib.auth.mixins import UserPassesTestMixin
from users.models import User

class AdminOrSuperUserMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_anonymous:
            return False
        return any(
            [
                self.request.user.role == User.SUPERADMIN,
                self.request.user.role == User.ADMIN,
                self.request.user.has_perm("users.add_parent"),
            ]
        )