from . import models
from rest_framework import serializers


class EmploymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EmploymentType
        fields = '__all__'


class ParametersSerializer(serializers.HyperlinkedModelSerializer):
    employmenttype = EmploymentTypeSerializer(many=True)

    class Meta:
        model = models.Parameters
        fields = ('age', 'growth', 'clothsize', 'chestsize', 'waistsize', 'thighsize', 'footsize',
                  'necksize', 'headsize', 'tatu', 'piercing', 'appearancetype',
                  'haircolor', 'city', 'employmenttype', 'eyecolor', 'gender', 'country')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


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


class PortfolioElemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PortfolioElem
        fields = '__all__'


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'


class AppearanceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AppearanceType
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


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Role
        fields = '__all__'


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Request
        fields = '__all__'


class ContactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Contacts
        fields = '__all__'


class InviteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Invite
        fields = '__all__'


class RegistrySerializer(serializers.HyperlinkedModelSerializer):
    param_list = ParametersSerializer()
    contacts = ContactsSerializer()

    class Meta:
        model = models.Employee
        fields = ('contacts', 'firstname', 'lastname', 'param_list')

    def create(self, validated_data):
        contact_data = validated_data.pop('contacts')
        contacts = models.Contacts.objects.create(**contact_data)
        contacts.save()
        param_data = validated_data.pop('param_list')
        emp_type = param_data.pop('employmenttype')
        params = models.Parameters.objects.create(**param_data)
        params.save()
        for et in emp_type:
            params.employmenttype.add(et)
        firstname = validated_data.pop('firstname')
        lastname = validated_data.pop('lastname')
        employee = models.Employee.objects.create(firstname=firstname, lastname=lastname, param_list=params, contacts=contacts)
        employee.save()
        return employee

    def update(self, instance, validated_data):
        validated_data_param_list = validated_data.get('param_list', instance.param_list)
        instance.param_list.clothsize = validated_data_param_list.get('clothsize', instance.param_list.clothsize)
        instance.param_list.chestsize = validated_data_param_list.get('chestsize', instance.param_list.chestsize)
        instance.param_list.waistsize = validated_data_param_list.get('waistsize', instance.param_list.waistsize)
        instance.param_list.thighsize = validated_data_param_list.get('thighsize', instance.param_list.thighsize)
        instance.param_list.footsize = validated_data_param_list.get('footsize', instance.param_list.footsize)
        instance.param_list.necksize = validated_data_param_list.get('necksize', instance.param_list.necksize)
        instance.param_list.headsize = validated_data_param_list.get('headsize', instance.param_list.headsize)
        instance.param_list.tatu = validated_data_param_list.get('tatu', instance.param_list.tatu)
        instance.param_list.piercing = validated_data_param_list.get('piercing', instance.param_list.piercing)
        return instance


class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Review
        fields = '__all__'


class ReviewRegistrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Review
        fields = ('employee', 'professional_skills', 'human_skills')

    def create(self, validated_data):
        print(validated_data)
        return self
