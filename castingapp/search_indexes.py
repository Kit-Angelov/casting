from haystack import indexes
from . import models


class EmployeesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    firstname = indexes.CharField(model_attr='firstname')
    lastname = indexes.CharField(model_attr='lastname')

    def get_model(self):
        return models.Employee

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
