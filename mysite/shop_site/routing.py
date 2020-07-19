from django.urls import re_path
from . import consumers
websocket_urlpatterns = [
    re_path(r'ws/shop/product/(?P<auth_id>\d+)/$', consumers.ShopSiteConsumer),
]
