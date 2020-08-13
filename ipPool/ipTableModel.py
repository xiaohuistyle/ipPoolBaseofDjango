from django.http import HttpResponse

from IpModel.models import IpModel


# 数据库操作
# 向数据库中添加数据 返回添加成功或者失败
def Add(ipAddress, port):
    IsExist = IpModel.objects.filter(Address=ipAddress, port=port)
    if(IsExist):
        IP = IpModel(Address=ipAddress, port=port)
        IP.save()
        return True
    else:
        return False




