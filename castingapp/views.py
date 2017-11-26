from . import models
from rest_framework import viewsets
from . import serializers
# from . import filters
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.parsers import FileUploadParser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import Filters
from django_filters import rest_framework

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class ParametersViewSet(viewsets.ModelViewSet):

    queryset = models.Parameters.objects.all()
    serializer_class = serializers.ParametersSerializer
    # filter_class =


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class HairColorViewSet(viewsets.ModelViewSet):

    queryset = models.HairColor.objects.all()
    serializer_class = serializers.HairColorSerializer


class CityViewSet(viewsets.ModelViewSet):

    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class GenderViewSet(viewsets.ModelViewSet):

    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderSerializer


class PortfolioElemViewSet(viewsets.ModelViewSet):

    queryset = models.PortfolioElem.objects.all()
    serializer_class = serializers.PortfolioElemSerializer


class CountryViewSet(viewsets.ModelViewSet):

    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class EyeColorViewSet(viewsets.ModelViewSet):

    queryset = models.EyeColor.objects.all()
    serializer_class = serializers.EyeColorSerializer


class AppearanceTypeViewSet(viewsets.ModelViewSet):

    queryset = models.AppearanceType.objects.all()
    serializer_class = serializers.AppearanceTypeSerializer


class EmploymentTypeViewSet(viewsets.ModelViewSet):

    queryset = models.EmploymentType.objects.all().filter(original=True)
    serializer_class = serializers.EmploymentTypeSerializer


class EmployerViewSet(viewsets.ModelViewSet):

    queryset = models.Employer.objects.all()
    serializer_class = serializers.EmployerSerializer


class CastingTypeViewSet(viewsets.ModelViewSet):

    queryset = models.CastingType.objects.all()
    serializer_class = serializers.CastingTypeSerializer


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer


class CastingViewSet(viewsets.ModelViewSet):

    queryset = models.Casting.objects.all()
    serializer_class = serializers.CastingSerializer


class RoleViewSet(viewsets.ModelViewSet):

    queryset = models.Role.objects.all()
    serializer_class = serializers.RoleSerializer


class RequestViewSet(viewsets.ModelViewSet):

    queryset = models.Request.objects.all()
    serializer_class = serializers.RequestSerializer


class InviteViewSet(viewsets.ModelViewSet):

    queryset = models.Invite.objects.all()
    serializer_class = serializers.InviteSerializer


class ContactsViewSet(viewsets.ModelViewSet):

    queryset = models.Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer


class EmployeeReg(viewsets.ModelViewSet):

    queryset = models.Employee.objects.all()
    serializer_class = serializers.RegisterEmployeeSerializer


class EmployerReg(viewsets.ModelViewSet):
    queryset = models.Employer.objects.all()
    serializer_class = serializers.RegisterEmployerSerializer


@api_view(["POST"])
def login(request):
    print(request.user)
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


@api_view(["POST"])
def testview(request):
    print('request', request.user)
    user_id = int(request.data.get('user_id'))
    age = int(request.data.get('age'))
    growth = int(request.data.get('growth'))
    clothsize = int(request.data.get('clothsize'))
    chestsize = int(request.data.get('chestsize'))
    waistsize = int(request.data.get('waistsize'))
    thighsize = int(request.data.get('thighsize'))
    footsize = int(request.data.get('footsize'))
    necksize = int(request.data.get('necksize'))
    headsize = int(request.data.get('headsize'))
    tatu = request.data.get('tatu')
    piercing = request.data.get('piercing')
    appearancetype = int(request.data.get('appearancetype'))
    haircolor = int(request.data.get('haircolor'))
    city = int(request.data.get('city'))
    eyecolor = request.data.get('eyecolor')
    gender = request.data.get('gender')
    country = request.data.get('country')
    employmenttype = request.data.get('employmenttype')

    if tatu == 'true': tatu = True
    else: tatu = False
    if piercing == 'true': piercing = True
    else: piercing = False

    user = User.objects.get(id=user_id)
    appearancetype_obj = models.AppearanceType.objects.get(id=appearancetype)
    haircolor_obj = models.HairColor.objects.get(id=haircolor)
    city_obj = models.City.objects.get(id=city)
    eyecolor_obj = models.EyeColor.objects.get(id=eyecolor)
    gender_obj = models.Gender.objects.get(id=gender)
    country_obj = models.Country.objects.get(id=country)
    list_empoymenttype_obj = list()
    for elem in employmenttype:
        try:
            elem = int(elem)
        except:
            pass
        if isinstance(elem, int):
            employmenttype_obj = models.EmploymentType.objects.get(id=elem)
            list_empoymenttype_obj.append(employmenttype_obj)
        elif isinstance(elem, str):
            employmenttype_obj = models.EmploymentType(name=elem, original=False)
            employmenttype_obj.save()
            list_empoymenttype_obj.append(employmenttype_obj)

    new_parameters = models.Parameters(age=age,
                                       growth=growth,
                                       clothsize=clothsize,
                                       chestsize=chestsize,
                                       waistsize=waistsize,
                                       thighsize=thighsize,
                                       footsize=footsize,
                                       necksize=necksize,
                                       headsize=headsize,
                                       tatu=tatu,
                                       piercing=piercing,
                                       appearancetype=appearancetype_obj,
                                       haircolor=haircolor_obj,
                                       city=city_obj,
                                       eyecolor=eyecolor_obj,
                                       gender=gender_obj,
                                       country=country_obj,
                                       user=user)

    new_parameters.save()
    for attr in list_empoymenttype_obj:
        new_parameters.employmenttype.add(attr)
    if not new_parameters:
        return Response({"error": "Parameters new failed"})
    return Response({'parameters_id': new_parameters.id})


class TestImgView(viewsets.ModelViewSet):
    queryset = models.TestImgModel.objects.all()
    serializer_class = serializers.TestImgSerializer


class ShowEmployeesPls(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeFullSerializer
    filter_class = Filters.F
    filter_backends = (rest_framework.DjangoFilterBackend,)


@api_view(["POST"])
def testimgviewnew(request):
    parser_classes = (FileUploadParser,)
    image = request.data['image']
    name = request.data['name']
    newImage = models.TestImgModel(name=name, image=image)
    newImage.save()
    return Response({'id': newImage.id})


class ShowCastingList(viewsets.ModelViewSet):
    queryset = models.Casting.objects.all()
    serializer_class = serializers.Casting2Serializer

