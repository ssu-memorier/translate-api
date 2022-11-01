from rest_framework import serializers
from .models import User

'''
    django REST framework에서 제공하는 serializer를 활용하여
    request로 받은 data를 역직렬화 하여 DB에 반영하고
    reponse로 사용 될 data를 다시 직렬화하여 json이나 xml등으로 손쉽게 변환이 가능하다.
'''


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # 모델 User의 모든 field를 serializer함.
