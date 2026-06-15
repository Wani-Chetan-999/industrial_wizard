import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('django_settings_module', 'industrial_wizard.settings')

django_asgi_app = get_asgi_application()

# We will import the routing configuration from chatbot app later
# For now, initialize the base structural framework
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter([])
    ),
})