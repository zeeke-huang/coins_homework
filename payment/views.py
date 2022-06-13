from .models import Payment
from rest_framework.decorators import action
from .serializers import PaymentSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
import sys
sys.path.append('..')
from user.models import User
from user.serializers import UserSerializer
from django.db import transaction

class PaymentViewSet(ViewSet):
    # API endpoint that allows creation of a new payment

    def list(self, request):
        queryset = Payment.objects.all()
        serializer = PaymentSerializer(queryset, many=True)
        for item in serializer.data:
            if item.get('from_account') is None:
                item = item.pop('from_account')
            else:
                item = item.pop('to_account')
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create_payment(self, request):
        from_account = request.data.get('from_account')
        to_account = request.data.get('to_account')
        amount = request.data.get('amount')

        try:
            queryset_from = User.objects.get(id=from_account)
            queryset_to = User.objects.get(id=to_account)
        except Exception as e:
            return Response({"msg": 'account does not exist'})

        from_serializers = UserSerializer(queryset_from)
        to_serializers = UserSerializer(queryset_to)
        from_currency = from_serializers.data.get('currency')
        to_currency = to_serializers.data.get('currency')
        from_balance = from_serializers.data.get('balance')
        to_balance = to_serializers.data.get('balance')
        if from_currency != to_currency:
            return Response({"msg": 'different currencies'})

        from_balance - amount
        if (from_balance - amount) < 0:
            return Response({"msg": 'balance is not enough'})
        else:
            try:
                with transaction.atomic():
                    queryset_from.balance = from_balance - amount
                    queryset_to.balance = to_balance + amount
                    queryset_from.save()
                    queryset_to.save()
                    pay1 = Payment(
                        account = request.data.get('from_account'),
                        to_account = request.data.get('to_account'),
                        amount = request.data.get('amount'),
                        direction = 'outgoing'
                    )
                    pay2 = Payment(
                        account = request.data.get('to_account'),
                        from_account = request.data.get('from_account'),
                        amount = request.data.get('amount'),
                        direction = 'incoming'
                    )
                    pay1.save()
                    pay2.save()
            except Exception as e:
                return Response({"msg": 'fail'})
        return Response({"msg": 'ok'})
