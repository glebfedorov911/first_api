from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .backends import AuthBackend
from .serializers import *
from .models import *


class SignUpAPI(APIView):
    serializers = ProfileSerializer
    query_set = get_user_model()
    permission_classes = (AllowAny, )

    def post(self, request):
        serializers = ProfileSerializer(data=request.data)

        if request.data.get('password') == request.data.get('re_password'):
            serializers.is_valid(raise_exception=True)
            serializers.save()

            return Response({'post': serializers.data, 'data': 'post successful'})

        return Response({'post': 'error', 'data': 'post unsuccessful'})

class LoginAPI(APIView):
    backend = AuthBackend()
    permission_classes = (AllowAny, )

    def post(self, request):
        user = self.backend.authenticate(request, **request.data)

        if user is None:
            return Response({'post': 'error', 'data': 'undefinied user'})

        tkn = Token.objects.get_or_create(user=self.backend.get_user(user.id))[0].key

        return Response({'post': tkn, 'data': 'post successful'})

    def delete(self, request):
        current_user = request.user
        Token.objects.filter(user=current_user).delete()

        return Response({'delete': 'unauth', 'data': 'delete successful'})

class GoodsAPI(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        if request.GET.get('goods', None):
            rates = Rating.objects.filter(good=request.GET.get('goods'))
            rates_sum = sum(list(map(lambda x: int(x.rate), rates)))
            rates_sr = round(rates_sum/len(rates))

            return Response({'rates': rates_sr})

        goods = Goods.objects.all()
        return Response({'get': [{'name': good.name, 'desc': good.desc, 'cost':good.cost}] for good in goods})

    def post(self, request):
        current_user = request.user
        good = Goods.objects.get(id=request.data.get('goods'))

        if current_user.id is None:
            return Response({'post': 'error', 'data': 'post unsuccessful'})

        if not request.data.get('count', None) is None:
            user = User.objects.get(id=current_user.id)
            count = request.data.get('count')

            try:
                good_add = self.get_basket_data(user, good)
                Basket.objects.update(user=user, goods=good, count=good_add.count+count)
            except:
                good_add = Basket.objects.create(user=user, goods=good, count=count)
                good_add.save()

            return Response({'post': {"user": user.id, "goods": good.id, "count": good_add.count+count}, 'data': 'post successful'})

        elif not request.data.get('rate', None) is None:
            rate = request.data.get('rate')
            good_add = Rating.objects.create(rate=rate, good=good)
            good_add.save()

            return Response({'post': {"rate": good_add.rate, "goods": good.id}, 'data': 'post successful'})

        return Response({'post': 'error', 'data': 'post unsuccessful'})

    def get_basket_data(self, user, good):
        return Basket.objects.get(user=user, goods=good)

class ProfileAPI(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if int(request.GET.get('id')) != int(request.user.id):
            return Response({'get': 'error', 'data': 'get unsuccessful'})

        user = User.objects.get(id=request.GET.get('id'))
        return Response({
            'firstname': user.firstname, "surname": user.surname, "phone": user.phone, "email": user.email,
            "inst": user.inst, 'address': user.address, 'city': user.city, 'country': user.country, 'index': user.index})

    def put(self, request, *args, **kwargs):
        if int(request.data.get('id')) != int(request.user.id):
            return Response({'post': 'error', 'data': 'post unsuccessful'})

        try:
            instance = User.objects.get(id=request.data.get('id'))
        except:
            return Response({'post': 'error', 'data': 'post unsuccessful'})

        request.data['password'] = '12345678'
        serializers = ProfileSerializer(data=request.data, instance=instance)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response({'post': serializers.data, 'data': 'put successful'})
