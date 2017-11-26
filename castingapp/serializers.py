from . import models
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
UserModel = get_user_model()
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password


class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Review
        fields = '__all__'


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class PortfolioElemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PortfolioElem
        fields = '__all__'


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'


class EyeColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EyeColor
        fields = '__all__'


class EmployerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employer
        fields = '__all__'


class CastingTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CastingType
        fields = '__all__'


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Payment
        fields = '__all__'


class CastingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Casting
        fields = '__all__'


class CastingNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Casting
        fields = ('name',)


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    casting = CastingSerializer()

    class Meta:
        model = models.Role
        fields = ('id', 'name', 'salary', 'start_date', 'expire_date', 'description', 'casting')


class Casting2Serializer(serializers.HyperlinkedModelSerializer):
    role_set = RoleSerializer(many=True)

    class Meta:
        model = models.Casting
        fields = ('id', 'name', 'role_set')


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Request
        fields = '__all__'


class ContactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Contacts
        fields = '__all__'


class EmployeeNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('username',)


class EmployerNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employer
        fields = ('username',)


class RoleNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Role
        fields = ('name',)


class InviteSerializer(serializers.HyperlinkedModelSerializer):
    employee = EmployeeNameSerializer()
    creator = EmployerNameSerializer()
    role = RoleNameSerializer()

    class Meta:
        model = models.Invite
        fields = ('id', 'creation_date', 'employee', 'creator', 'role')


class HairColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.HairColor
        fields = '__all__'


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Gender
        fields = '__all__'


class AppearanceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AppearanceType
        fields = '__all__'


class EmploymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EmploymentType
        fields = '__all__'


class ParametersSerializer(serializers.HyperlinkedModelSerializer):
    employmenttype = EmploymentTypeSerializer(many=True)
    appearancetype = AppearanceTypeSerializer(many=False)
    haircolor = HairColorSerializer(many=False)
    eyecolor = EyeColorSerializer(many=False)
    gender = GenderSerializer(many=False)
    city = CitySerializer(many=False)
    country = CountrySerializer(many=False)

    class Meta:
        model = models.Parameters
        fields = ('age', 'growth', 'clothsize', 'chestsize', 'waistsize', 'thighsize', 'footsize',
                  'necksize', 'headsize', 'tatu', 'piercing', 'appearancetype',
                  'haircolor', 'city', 'employmenttype', 'eyecolor', 'gender', 'country')


class ReviewRegistrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Review
        fields = ('employee', 'professional_skills', 'human_skills')

    def create(self, validated_data):
        print(validated_data)
        return self


# class RegisterUserSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('password', 'username')
#
#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(raw_password=password)
#         instance.save()
#         group = Group.objects.get(id=1)
#         instance.groups.add(group)
#         return instance


class TestImgSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.FileField()

    class Meta:
        model = models.TestImgModel
        fields = ('name', 'image')


class RegisterEmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Employee
        fields = ('password', 'username')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(raw_password=password)
        instance.save()
        group = Group.objects.get(id=1)
        instance.groups.add(group)
        return instance


class RegisterEmployerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Employer
        fields = ('password', 'username')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(raw_password=password)
        instance.save()
        group = Group.objects.get(id=1)
        instance.groups.add(group)
        return instance


class EmployeeFullSerializer(serializers.HyperlinkedModelSerializer):

    param_list = ParametersSerializer

    class Meta:
        model = models.Employee
        fields = ('username', 'param_list', 'check_params')
