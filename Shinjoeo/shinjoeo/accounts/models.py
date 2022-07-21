from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def get_username(self):
        return str(self.username)

User.add_to_class("__str__",get_username)