"""onlinestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from greetings.views import GoodMorningView,GoodAfternoonView
from products.views import ProductsView,ProductDetailView
# localhost:8000/morning/
#localhost:8000/after/
#localhost:products/2
urlpatterns = [
    path('admin/', admin.site.urls),
    path("morning/",GoodMorningView.as_view()),
    path("after/",GoodAfternoonView.as_view()),
    path("products/",ProductsView.as_view()),
    path("products/<int:id>/",ProductDetailView.as_view())


]
