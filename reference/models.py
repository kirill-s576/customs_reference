from django.db import models

# Create your models here.


class Country(models.Model):
    country_id = models.IntegerField()
    country_class = models.IntegerField()
    code = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    ondate = models.DateTimeField(null=True)
    offdate = models.DateTimeField(null=True)
    issystem = models.IntegerField()
    basison = models.CharField(max_length=1000)
    basisoff = models.CharField(max_length=1000)
    short = models.CharField(max_length=1000)
    alpha2 = models.CharField(max_length=1000)
    alpha3 = models.CharField(max_length=1000)
    en = models.CharField(max_length=1000)
    updated = models.DateTimeField(auto_now=True)


class PaymentsType(models.Model):
    payment_id = models.IntegerField()
    payment_class = models.IntegerField()
    code = models.CharField(max_length=1000)
    ondate = models.DateTimeField(null=True)
    offdate = models.DateTimeField(null=True)
    issystem = models.IntegerField()
    basison = models.CharField(max_length=1000)
    basisoff = models.CharField(max_length=1000)
    longdesc = models.TextField(max_length=5000)
    paymenttype = models.IntegerField()
    direction = models.IntegerField()
    paymentcode = models.IntegerField()
    feature = models.CharField(max_length=1000)

    def incountrieslist(self):
        return InExCoutry.objects.filter(paymentstype=self, in_ex_type="incountry").values_list("country")

    def excountrieslist(self):
        return InExCoutry.objects.filter(paymentstype=self, in_ex_type="excountry").values_list("country")


class InExCoutry(models.Model):
    paymentstype = models.ForeignKey(PaymentsType, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    in_ex_type = models.CharField(max_length=1000)  # incountry or excountry






