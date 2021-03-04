from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer


@api_view()
def findProfile(request):
    """ Find the user based on card id and respond with success. Do not send
    data back as pin validation is required """

    card_id = request.query_params.get('cardid')
    queryset = Profile.objects.filter(card_id__exact=card_id)

    # if user found send status 200 else 404
    if queryset:
        return Response({"User Found"}, status.HTTP_200_OK)
    else:
        return Response({"Not Found"}, status.HTTP_404_NOT_FOUND)


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    models = Profile

    def partial_update(self, request, *args, **kwargs):
        """ Update balance by adding new value to current value """

        # Get amount form request and add it to current balance
        amount = request.data.get('balance')
        instance = self.get_object()
        new_balance = float(amount) + float(instance.balance)
        new_balance = "%.2f" % new_balance

        serializer = self.get_serializer(
            instance, {'balance': new_balance}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status.HTTP_200_OK)

    def get_queryset(self):
        """ Return record based on pin and card_id passed in the request or
        return all data on record creation/udate """

        card_id = self.request.query_params.get('cardid')
        pin = self.request.query_params.get('pin')

        if card_id and pin:
            queryset = Profile.objects.filter(card_id__exact=card_id)\
                .filter(pin__exact=pin)

            if queryset:
                return queryset
            else:
                return Response({'NOT FOUND'}, status.HTTP_404_NOT_FOUND)
        else:
            return Profile.objects.all()
