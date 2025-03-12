from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    """
    Modelo que representa el perfil de un usuario.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # on_delete=models.CASCADE significa que si el usuario es eliminado, también se eliminará su perfil.

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # upload_to='profile_pics' especifica el directorio donde se guardarán las imágenes.

    def __str__(self):

        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """
        Sobreescribe el método save para redimensionar las imágenes de perfil.

        """
        super().save(*args, **kwargs)
        # Llama al método save de la clase padre para guardar el perfil.

        img = Image.open(self.image.path)
        # Abre la imagen de perfil utilizando PIL.

        if img.height > 300 or img.width > 300:
            # Verifica si la imagen es más grande que 300x300 píxeles.

            output_size = (300, 300)
            # Define el tamaño de salida deseado.

            img.thumbnail(output_size)
            # Redimensiona la imagen utilizando thumbnail, manteniendo la relación de aspecto.

            img.save(self.image.path)
            # Guarda la imagen redimensionada
