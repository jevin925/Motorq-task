from django.db import models


class User(models.Model):
    name = models.TextField(max_length=200, null=False)
    email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return self.email


class subjects(models.Model):
    name = models.TextField(max_length=200, null=False, unique=True)
    available_seats = models.IntegerField(default=60,null=False)
    sub_day = models.TextField(max_length=12, null=False)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name

class waiting_list(models.Model):
    sub_id = models.ForeignKey(to=subjects, null=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(to=User, null=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('sub_id', 'user_id',)
    
class user_subject(models.Model):
    sub_id = models.ForeignKey(to=subjects, null=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(to=User, null=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('sub_id', 'user_id',)