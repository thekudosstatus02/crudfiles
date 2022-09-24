"""remind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from anne import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about/',views.About),
    path('search-topic/',views.searchTopic),
    path('search-topic-public/',views.searchTopicPublic),
    path('public-subject/',views.publicSubject),
    path('public-profile/',views.publicProfile),
    path('search/',views.searchUser),
    path('user-login/',views.signIn),
    path('view-subject/',views.viewSubject),
    path('user-login/',views.signIn),
    path('add-profile/',views.addProfile),
    path('view-profile/',views.viewProfile),
    path('edit-profile/',views.editProfile),
    path('update-profile/',views.updateProfile),
    path('edit-subject/',views.editSubject),
    path('update-subject/',views.updateSubject),
    path('add-subject/',views.addSubjct),
    path('edit-unit/',views.editUnit),
    path('update-unit/',views.updateUnit),
    path('add-unit/',views.addUnit),
    path('edit-topic/',views.editTopic),
    path('update-topic/',views.updateTopic),
    path('add-topic/',views.addTopic),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
