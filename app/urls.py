from django.conf import settings
from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Icecream Shop Admin"
admin.site.site_title = "Icecream Shop Admin Portal"
admin.site.index_title = "Welcome to Icecream Shop"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),

    # Services
    path('services/icecream/', views.icecream, name='icecream'),
    path('services/cone_and_bar/', views.cone_and_bar, name='cone_and_bar'),
    path('services/family_pack_and_cake/', views.family_pack_and_cake, name='family_pack_and_cake'),

]
# Static & Media settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
