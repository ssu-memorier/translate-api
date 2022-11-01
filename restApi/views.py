from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status

from rest_framework.decorators import api_view

# Create your views here.


from translate import getGoogleTrans


@api_view(["POST"])
def googleTranslate(request):
    user_serializer = UserSerializer(data=request.data)

    if user_serializer.is_valid():
        msg = user_serializer.data['message']
        src = user_serializer.data['source']
        tgt = user_serializer.data['target']

        result = getGoogleTrans.get_translate(msg, src, tgt)

        return Response(result, status=status.HTTP_200_OK)

    else:
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
