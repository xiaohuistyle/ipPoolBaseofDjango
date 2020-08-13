from django.conf.urls import url
 
from . import view, ipTableModel, SearchLayer

urlpatterns = [
    url('hello/', view.hello),
    url('login/', view.Login),
    url('index/', view.Index, name='index'),
    url('welcome/', view.Welcome, name='welcome'),
    #管理员路由
    url('admin_add/', view.admin_add, name='admin_add'),
    url('admin_cate/', view.admin_cate, name='admin_cate'),
    url('admin_edit/', view.admin_edit, name='admin_edit'),
    url('admin_list/', view.admin_list, name='admin_list'),
    url('admin_role/', view.admin_role, name='admin_role'),
    url('admin_rule/', view.admin_rule, name='admin_rule'),
    #城市
    url('cate/', view.cate, name='cate'),
    url('city/', view.city, name='city'),
    #t图表
    url('echart1/', view.echart1, name='echart1'),
    url('echart2/', view.echart2, name='echart2'),
    url('echart3/', view.echart3, name='echart3'),
    url('echart4/', view.echart4, name='echart4'),
    url('echart5/', view.echart5, name='echart5'),
    url('echart6/', view.echart6, name='echart6'),
    url('echart7/', view.echart7, name='echart7'),
    url('echart8/', view.echart8, name='echart8'),
    #会员管理
    url('member_add/', view.member_add, name='member_add'),
    url('member_del/', view.member_del, name='member_del'),
    url('member_edit/', view.member_edit, name='member_edit'),
    url('member_list/', view.member_list, name='member_list'),
    url('member_password/', view.member_password, name='member_password'),
    #订单管理
    url('order_add/', view.order_add, name='order_add'),
    url('order_list/', view.order_list, name='order_list'),
    url('role_add/', view.role_add, name='role_add'),
    url('unicode/', view.unicode, name='unicode'),
    #ip池功能
    url('ipMain/', view.ipMain, name='ipMain'),
    url('SearchIp/', SearchLayer.search_routers, name='SearchIp'),
]