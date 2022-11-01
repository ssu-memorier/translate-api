from django.db import models

# Create your models here.


class User(models.Model):
    message = models.CharField(max_length=10000, null=False)
    source = models.CharField(max_length=128, null=False)
    target = models.CharField(max_length=128, null=False)

    class Meta:
        # Table이름을 "User"로 정한다 default 이름은 api_user_user가 된다.
        db_table = "User"
