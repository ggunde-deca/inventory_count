from django.urls import path
from .views import (
    InventoryTrackerListApiView,
    InventoryTrackerDetailListApiView,
)

urlpatterns = [
    path("api", InventoryTrackerListApiView.as_view()),
    path("api/<item_name>/", InventoryTrackerDetailListApiView.as_view()),
]
