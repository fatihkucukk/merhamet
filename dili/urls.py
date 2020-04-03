from django.conf.urls import include, url
from dili import views


urlpatterns = [
    url('^$', views.AnaSayfaView.as_view(), name='anasayfa'),
    url('^erkek-yuzuk/$', views.ErkekYuzukView.as_view(), name='erkek_yuzuk'),
    url('^kadın-yuzuk/$', views.KadınYuzukView.as_view(), name='kadın_yuzuk'),
    url('^kupee/$', views.KupelerView.as_view(), name='kupeee'),
    url('^hakkında/$', views.HakkındaView.as_view(), name='hakkinda'),
    url('^komisyonlar/$', views.KomisyonView.as_view(), name='komisyonn'),
    url('^blog/$', views.BlogView.as_view(), name='blogu'),
]
