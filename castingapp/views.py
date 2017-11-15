from . import models
from rest_framework import viewsets
from . import serializers
# from . import filters


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

    queryset = models.EmploymentType.objects.all()
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


class RegistryViewSet(viewsets.ModelViewSet):

    queryset = models.Employee.objects.all()
    serializer_class = serializers.RegistrySerializer


class ContactsViewSet(viewsets.ModelViewSet):

    queryset = models.Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer


class ReviewRegViewSet(viewsets.ModelViewSet):

    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewRegistrySerializer
