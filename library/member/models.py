from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return 'Member : {} {}'.format(self.firstname,self.lastname)

class Avatar(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images')