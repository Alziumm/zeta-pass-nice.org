from django.urls import path
from django.views.decorators.csrf import requires_csrf_token
from listings import view

urlpatterns = [
    path('', requires_csrf_token(view.Home.as_view()), name = ''),
    path('home/', requires_csrf_token(view.Home.as_view()), name = 'home'),
    path('legal/', requires_csrf_token(view.Legal.as_view()), name = 'legal'),
    path('privacy-policy/', requires_csrf_token(view.Policy.as_view()), name = 'policy'),
]

handler400 = 'listings.middleware.error400'
handler401 = 'listings.middleware.error401'
handler403 = 'listings.middleware.error403'
handler404 = 'listings.middleware.error404'
handler500 = 'listings.middleware.error500'
handler504 = 'listings.middleware.error504'