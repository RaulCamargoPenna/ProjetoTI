from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings 



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')
app.conf.enable_utc = False

app.conf.update(timezone = 'America/Sao_Paulo',
                CELERYD_POOL_RESTARTS = True) #Habilitar o restart de pool pelo flower

app.config_from_object(settings, namespace='CELERY')


# CELERY ROUTES
app.conf.update(
    CELERY_ROUTES = {
        'setor_ti.tasks.send_info_to_websocket': {'queue': 'fila_rapida'},
    }
)

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

    