from django.urls import path
from . import views as tutorial_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', tutorial_views.index.as_view(), name='home'),
    path('api/tutorials/', tutorial_views.tutorial_list),
    path('api/tutorials/<int:pk>/', tutorial_views.tutorial_detail),
    path('api/tutorials/published/', tutorial_views.tutorial_list_pubished)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

