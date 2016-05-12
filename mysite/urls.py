"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from login import views as login_views
from register import views as register_views
from notice import views as notice_views
from question import views as question_views
from forum import views as forum_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register.html', register_views.register),
    url(r'^$', login_views.index),
    url(r'^logout.html', login_views.logout),
    url(r'^login.html', login_views.login),
    url(r'^notice.html', notice_views.view_notice),
    url(r'^details.html', notice_views.details),
    url(r'^add_notice.html', notice_views.add),
    url(r'^q&a.html', question_views.q_and_a),
    url(r'^add_question.html', question_views.add_question),
    url(r'^add_answer.html', question_views.add_answer),
    url(r'^forum.html', forum_views.view),
    url(r'^topic.html', forum_views.topic),
    url(r'^add_topic.html', forum_views.add_topic),
    url(r'^add_reply.html', forum_views.add_reply),
]
