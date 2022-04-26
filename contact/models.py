from django.db import models

# Create your models here.
class ContactModel(models.Model):
    """Модель обратной связи от пользователя"""

    name = models.CharField('Имя', max_length=50)
    email = models.EmailField()
    subject = models.CharField('Тема', max_length=100)
    message = models.TextField('Сообщение', max_length=3000)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'