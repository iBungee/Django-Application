# Django-Application
The purpose is this repo is to learn Django

Tutorial based on youtube playlist [Django Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

Create admin user
`python3 manage.py migrate && python3 manage.py makemigrations`
`python3 manage.py createsuperuser`

Create normal user
`python3 manage.py shell`
```python3
from django.contrib.auth.models import User
user = User.objects.create_user('test', password='test')
user.is_superuser=False
user.is_staff=False
user.save()
```

Start a new app