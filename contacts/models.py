from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PhoneNumber(models.Model):
    number = models.CharField(max_length=255)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='numbers')

    class Meta:
        unique_together = (("number", "contact"),)
