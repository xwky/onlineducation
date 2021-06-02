from haystack import indexes
from .models import *


# 对指定的某个类的某些字段建立索引
class CourseIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True) #有且只有一个
    # 对名称、标签、详情进行搜索
    name = indexes.CharField(model_attr='name')
    desc = indexes.CharField(model_attr='desc')
    detail = indexes.CharField(model_attr='detail')

    def get_model(self):
        return Course

    def index_queryset(self, using=None):
        return self.get_model().objects.all()