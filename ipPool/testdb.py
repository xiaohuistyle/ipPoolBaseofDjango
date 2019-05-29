from django.http import HttpResponse

from IpModel.models import IpModel


# 数据库操作
def testdb(request):
    test1 = IpModel(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")