from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('', UserViewSet)


urlpatterns = [
    path('', signIn, name='login'),
    path('logout/<int:pk>/', signOUT, name='logout'),
    path('auth/', include(router.urls), name='auth'),
    path('enquiry/list/', EnquiryListView.as_view(), name='enquiry_list'),
    path('enquiry/create/', EnquiryCreateView.as_view(), name='enquiry_create'),
    path('enquiry/update/<int:pk>/', EnquiryUpdateView.as_view(), name='enquiry_update'),
    path('enquiry/detail/<int:pk>/', EnquiryDetailView.as_view(), name='enquiry_detail'),
    path('equipment/list/', EquipmentListView.as_view(), name='equipment_list'),
    path('equipment/create/', EquipmentCreateView.as_view(), name='equipment_create'),
    path('equipment/update/<int:pk>/', EquipmentUpdateView.as_view(), name='equipment_update'),
    path('equipment/detail/<int:pk>/', EquipmentDetailView.as_view(), name='equipment_detail'),
    path('plan/list/', PlanListView.as_view(), name='plan_list'),
    path('plan/create/', PlanCreateView.as_view(), name='plan_create'),
    path('plan/update/<int:pk>/', PlanUpdateView.as_view(), name='plan_update'),
    path('plan/detail/<int:pk>/', PlanDetailView.as_view(), name='plan_detail'),
    path('member/list/', MemberListView.as_view(), name='member_list'),
    path('member/create/', MemberCreateView.as_view(), name='member_create'),
    path('member/update/<int:pk>/', MemberUpdateView.as_view(), name='member_update'),
    path('member/detail/<int:pk>/', MemberDetailView.as_view(), name='member_detail'),   
]