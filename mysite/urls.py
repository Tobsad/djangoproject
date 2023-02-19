"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
#agregamos el include para poder traer las vistas de otro archivo url de las aplicaciones
from django.urls import path,include

#asi se importa solo una funcion
from myapp.views import vista_compuesta
# importando todo el archivo views.py


urlpatterns = [
    path('admin/', admin.site.urls),
    #aqui estaran todas las vistas de urls del aplicativo, en este caso myapp
    path('', include('myapp.urls')),
    
]
