from django.db.models.signals import post_save
from django.dispatch import receiver
import random
from user.models import Cuenta, User

@receiver(post_save, sender=User)
def crear_cuenta(sender, instance, created, **kwargs):

    if created:

        numero_aleatorio = random.randint(0, 9999999999999999)
        n_cuenta = f'0881{str(numero_aleatorio).zfill(16)}'

        cuenta_nueva = Cuenta.objects.create(
            n_cuenta=n_cuenta,
            user_fk=instance,
        )
        cuenta_nueva.save()