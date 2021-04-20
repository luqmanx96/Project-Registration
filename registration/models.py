from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name


class Student(models.Model):

    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    # ic = models.CharField(max_length=15, help_text='Format 780506-10-4554.')
    date_of_birth = models.DateField(default=None)
    email = models.EmailField(max_length=100, null=True)
    adress_line_1 = models.CharField(max_length=100, null=True)
    adress_line_2 = models.CharField(max_length=100, null=True)
    poscode = models.CharField(max_length=5, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    contact_number = models.CharField(max_length=20, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
