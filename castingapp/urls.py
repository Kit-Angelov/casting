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
from rest_framework.authtoken import views as rest_framework_views

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
# router.register(r'register', views.RegistryViewSet)
router.register(r'contacts', views.ContactsViewSet)
# router.register(r'reviews', views.ReviewRegViewSet)
router.register(r'testimg', views.TestImgView)
router.register(r'regemployee', views.EmployeeReg)
router.register(r'regemployer', views.EmployerReg)
router.register(r'showemployees', views.ShowEmployeesPls)
router.register(r'castinglist', views.ShowCastingList)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', views.login),
    # url(r'^logout/$', views.logout_user, name='logout'),
    # url(r'^auth/$', views.login_form, name='login_form'),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^testview/$', views.testview, name='testview'),
    url(r'^testimgviewnew/$', views.testimgviewnew, name='testimgviewnew'),
]
