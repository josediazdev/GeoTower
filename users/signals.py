from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Crea un perfil de usuario automáticamente después de que se crea un nuevo usuario.

    Args:
        sender: El modelo que envía la señal (User).
        instance: La instancia del modelo que se está guardando (el nuevo usuario).
        created: Un booleano que indica si la instancia se creó (True) o se actualizó (False).
        **kwargs: Argumentos de palabra clave adicionales.
    """
    if created:
        # Verifica si el usuario fue creado recientemente.
        Profile.objects.create(user=instance)
        # Crea un nuevo perfil asociado al usuario recién creado.


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Guarda el perfil de usuario automáticamente después de que se guarda un usuario.

    Args:
        sender: El modelo que envía la señal (User).
        instance: La instancia del modelo que se está guardando (el usuario).
        **kwargs: Argumentos de palabra clave adicionales.
    """
    instance.profile.save()
    # Guarda el perfil asociado al usuario. Esto asegura que los cambios en el perfil se persistan.
    # Es necesario porque la señal post_save para User se dispara antes que la señal post_save para Profile.
