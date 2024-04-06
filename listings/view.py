#!/usr/bin/env python
# -*- coding: utf-8 -*-
from requests import get
from django.shortcuts import redirect, render
from django.views.generic import View
from django.conf import settings

class Public(View):

    default = {
        'title': None,
        'path': None,
        'template': None,
        'desc': None,
        'required_method': None,
    }

    def rendering(self, request):

        d_1 = ""
        d_2 = ""

        if request.session.get('STATUS', None) != None:

            d_1 = list(request.session.get('STATUS'))[0]
            d_2 = list(request.session.get('STATUS'))[1]

        return render(
            request, 
            self.default.get('template'),
            {   
                'status': d_1,
                'status_color': d_2,
                'default_language' : 'FR',
                'default_title' : f"ZETA-PASS-NICE > {self.default.get('title', '')}",
                'description': self.default.get('desc', ''),
            }
        )

    def get(self, request):

        return self.rendering(request)

    def post(self, request):

        if self.default.get('path') in ['', '/', 'home'] and request.POST.get('name', None) != None and request.POST.get('email', None) != None and request.POST.get('message', None) != None:

            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            if isinstance(name, str) == False or isinstance(email, str) == False or isinstance(message, str) == False or len(name) >= 65 or len(email) >= 65 or len(message) >= 1025:

                request.session['STATUS'] = ['Invalid contact data.', 'red']

                return redirect(self.default.get('path', '') + "#contact")

            try:
                get(f"{str(settings.TELEGRAM_ENDPOINT)}{f'Name : {str(name)} ||| Email : {str(email)} ||| Message : {str(message)}'}", headers={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3","Accept-Encoding": "gzip, deflate, sdch, br","Connection": "keep-alive"}, timeout=7500)
            except:
                pass

            request.session['STATUS'] = ['Votre message a bien été transmis à nos équipes.', 'green']

            return redirect(self.default.get('path', '') + "#contact")

        request.session['STATUS'] = ['Invalid form.', 'red']

        return redirect('error')

    def http_method_not_allowed(self, request):

        return redirect('error')

class Home(Public):

    default = {
        'title' : "Home", 
        'path' : "/", 
        'template' : "listings/home.html",
        'desc' : "ZETA-PASS-NICE est une association française quiu vise à lutter contre la précarité étudiante.",
        'required_method': ['GET', 'POST'],
    }

class Legal(Public):

    default = {
        'title' : "Mentions Legales", 
        'path' : "legal", 
        'template' : "listings/legal.html", 
        'desc' : "Mentions légales du site de l'association ZETA-PASS-NICE.",
        'required_method': ['GET'],
    }

class Policy(Public):

    default = {
        'title' : "Privacy Policy", 
        'path' : "policy", 
        'template' : "listings/policy.html", 
        'desc' :  "Politique de confidentialité du site de l'association ZETA-PASS-NICE.",
        'required_method': ['GET'],
    }