from django.db import models


class Data(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    expire_in = models.CharField(max_length=100 , null=True , blank=True)

    class Meta:
        verbose_name = "Data"
        verbose_name_plural = "Data"

    def __str__(self):
        return "Key : {} , Value : {}".format(self.key,self.value)