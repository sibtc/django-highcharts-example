from django.db import models

class Passenger(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )

    CHERBOURG = 'C'
    QUEENSTOWN = 'Q'
    SOUTHAMPTON = 'S'
    PORT_CHOICES = (
        (CHERBOURG, 'Cherbourg'),
        (QUEENSTOWN, 'Queenstown'),
        (SOUTHAMPTON, 'Southampton'),
    )

    name = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    survived = models.BooleanField()
    age = models.FloatField(null=True)
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=1, choices=PORT_CHOICES)

    def __str__(self):
        return self.name
