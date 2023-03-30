from django.contrib.auth.models import User
new_user = User()
new_user.username = 'user'
new_user.is_superuser = False
new_user.set_password('ornstein89')
new_user.save()