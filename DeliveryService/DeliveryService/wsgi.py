"""
WSGI config for DeliveryService project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
# standard
import os
from django.core.wsgi import get_wsgi_application

# additional
from django.db.backends.signals import connection_created
from django.dispatch import receiver

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DeliveryService.settings')
application = get_wsgi_application()


# time restriction for SQL request
@receiver(connection_created)
def setup_postgres(connection, **kwargs):
    if connection.vendor != 'postgresql':
        return

    # time out 30 seconds.
    with connection.cursor() as cursor:
        cursor.execute("""
            SET statement_timeout TO 30000;
        """)
