from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Question(models.Model):
    question = models.CharField(max_length=255)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Author: {self.author.username}, question: {self.question}'

    def get_absolute_url(self):
        """
        Devuelve la URL absoluta para la página de detalles de la pregunta.

        Returns:
            La URL para la página de detalles de la pregunta.
        """
        return reverse('forum:question-detail', kwargs={'pk': self.pk})
        # Utiliza la función reverse para generar la URL a partir del nombre de la vista ('forum:question-detail')
        # y los argumentos de palabra clave (pk=self.pk, donde pk es la clave primaria de la pregunta).


class Response(models.Model):
    response = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    base_question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'Author: {self.author.username}, question: {self.base_question}, response: {self.response}'
