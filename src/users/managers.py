from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Адрес электронной почты обязателен!')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        if user.is_superuser:
            phone = user.phone
            user.phone = f'+7 ({phone[2:5]}) {phone[5:8]}-{phone[8:10]}-{phone[10:]}'
        user.save(using=self.db)
        return user
    
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'Администратор')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)
