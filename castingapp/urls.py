"""blackjack_whores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from rest_framework import routers
from castingapp import views

router = routers.DefaultRouter()
router.register(r'parameters', views.ParametersViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'haircolor', views.HairColorViewSet)
router.register(r'city', views.CityViewSet)
router.register(r'gender', views.GenderViewSet)
router.register(r'portfolioelem', views.PortfolioElemViewSet)
router.register(r'country', views.CountryViewSet)
router.register(r'eyecolor', views.EyeColorViewSet)
router.register(r'appearancetype', views.AppearanceTypeViewSet)
router.register(r'employmenttype', views.EmploymentTypeViewSet)
router.register(r'employer', views.EmployerViewSet)
router.register(r'castingtype', views.CastingTypeViewSet)
router.register(r'payment', views.PaymentViewSet)
router.register(r'casting', views.CastingViewSet)
router.register(r'role', views.RoleViewSet)
router.register(r'request', views.RequestViewSet)
router.register(r'invite', views.InviteViewSet)
router.register(r'register', views.RegistryViewSet)
router.register(r'contacts', views.ContactsViewSet)
router.register(r'reviews', views.ReviewRegViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
