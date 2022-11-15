import re
from django.http import JsonResponse
from django.contrib.auth import get_user_model, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView, CreateAPIView,
    RetrieveAPIView, DestroyAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny
)
from .models import *
from .serializers import *


@csrf_exempt
def signIn(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
            return JsonResponse({'error': 'Please enter a valid password'})
        if len(password) < 6 :
            return JsonResponse({'error': 'Password must be atleast 6 characters long'})

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(email = username)
            if user.check_password(password):
                get_user = UserModel.objects.filter(email = username).values().first()
                get_user.pop('password')
                user.save()
                login(request=request, user=user)
            else:
                return JsonResponse({'error': 'Invalid Password'})
        except:
            return JsonResponse({'error': 'Invalid Email'})
    return JsonResponse({'error': 'Method not allowed!'})


@csrf_exempt
def signOUT(request, id):

    logout(request)

    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk = id)
        user.session_token = '0'
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user'})
    return JsonResponse({'Success': 'Sucessfully logged out'})


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

    def get_permissions(self):
        
        permission_class = []
        if self.action == 'create' or self.action == 'reterive':
            permission_class = [AllowAny]
        elif self.action == 'reterive' or self.action == 'update' or self.action == 'partial_update':
            permission_class = [IsAuthenticated]
        elif self.action == 'list' or self.action == 'destroy':
            permission_class = [IsAdminUser]
        return [permission() for permission in permission_class]


class EnquiryListView(ListAPIView):

    queryset = Enquiry.objects.all().order_by('-id')
    serializer_class = EnquirySerializer
    permission_classes = [IsAdminUser]


class EnquiryCreateView(CreateAPIView):

    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer
    permission_classes = [AllowAny]


class EnquiryUpdateView(RetrieveUpdateAPIView):

    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer
    permission_classes = [IsAuthenticated]


class EnquiryDetailView(RetrieveAPIView):

    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer
    permission_classes = [IsAdminUser]


class EquipmentListView(ListAPIView):

    queryset = Equipment.objects.all().order_by('-id')
    serializer_class = EquipmentSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class EquipmentCreateView(CreateAPIView):

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAdminUser]


class EquipmentUpdateView(RetrieveUpdateAPIView):

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAdminUser]


class EquipmentDetailView(RetrieveAPIView):

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAdminUser]


class PlanListView(ListAPIView):

    queryset = Plan.objects.all().order_by('-id')
    serializer_class = PlanSerializer
    permission_classes = [AllowAny]


class PlanCreateView(CreateAPIView):

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAdminUser]


class PlanUpdateView(RetrieveUpdateAPIView):

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAdminUser]


class PlanDetailView(RetrieveAPIView):

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [AllowAny]


class MemberListView(ListAPIView):

    queryset = Member.objects.all().order_by('-id')
    serializer_class = MemberSerializer
    permission_classes = [AllowAny]


class MemberCreateView(CreateAPIView):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAdminUser]


class MemberUpdateView(RetrieveUpdateAPIView):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAdminUser]


class MemberDetailView(RetrieveAPIView):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [AllowAny]

