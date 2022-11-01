from rest_framework.response import Response
from .serializers import RequestSerializer
from rest_framework import status

from rest_framework.decorators import api_view

from translate import googleTrans


@api_view(["POST"])
def googleTranslate(request):
    user_serializer = RequestSerializer(data=request.data)

    if user_serializer.is_valid():
        try:
            msg, src, tgt = user_serializer.data.values()
            result = googleTrans.get_translate(msg, src, tgt)

            return Response(result, status=status.HTTP_200_OK)
        except ValueError:
            return Response(user_serializer.error_messages["invalid"], status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
