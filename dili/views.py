from typing import Dict, Any

from django.db.models import QuerySet
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView


# Create your views here.
from dili.models import Ben


class AnaSayfaView(TemplateView):
    template_name = 'anasayfa.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proje = Ben.objects.all()
        context['proje'] = proje
        return context


class ErkekYuzukView(TemplateView):
    template_name = 'erkek_yuzukler.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        eyuzuk = Ben.objects.all()
        context['eyuzuk'] = eyuzuk
        return context


class KadınYuzukView(TemplateView):
    template_name = 'kadın_yuzukler.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kyuzuk = Ben.objects.all()
        context['kyuzuk'] = kyuzuk
        return context


class KupelerView(TemplateView):
    template_name = 'kupeler.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kupe = Ben.objects.all()
        context['kupe'] = kupe
        return context


class HakkındaView(TemplateView):
    template_name = 'hakkında.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hakkinda = Ben.objects.all()
        context['hakkinda'] = hakkinda
        return context


class KomisyonView(TemplateView):
    template_name = 'komisyon.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        komısyon = Ben.objects.all()
        context['komısyon'] = komısyon
        return context


class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogg = Ben.objects.all()
        context['blogg'] = blogg
        return context