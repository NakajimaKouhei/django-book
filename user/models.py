from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class  m_empUserManager(BaseUserManager):
    def create_user(self, emp_num, email_address, password):
        if not email_address:
            raise ValueError('メールアドレスを入力してください。')
        user = self.model(
            emp_num = emp_num,
            email_address = email_address,
            password = password,
            )
        user.set_password(password)
        user.save(UserWarning=self._db)
        return user

    def create_superuser(self, emp_num, email_address, password):
        user = self.create_user(emp_num, email_address, password)
        user.is_superuser = True
        user.save(UserWarning=self._db)
        return user

class m_emp(AbstractBaseUser):
    emp_num = models.CharField(max_length=5, unique=True, primary_key=True)
    email_address = models.CharField(max_length=255)

    USERNAME_FIELD = 'emp_num'
    REQUIRED_FIELDS = ['password']
    objects = m_empUserManager()