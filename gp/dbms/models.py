from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    permission = models.CharField(max_length=1)


class Djbasicnatu(models.Model):
    alloy_grade = models.CharField(max_length=255, null=True)
    chem_formula = models.CharField(max_length=255, null=True)
    main_elem  = models.CharField(max_length=255)
    second_elem  = models.CharField(max_length=255)
    trace_elem  = models.CharField(max_length=255, null=True)
    literature = models.CharField(max_length=255, null=True)
    info_source = models.CharField(max_length=255, null=True)
    structure_Id  = models.CharField(max_length=255, null=True)
    space_group = models.CharField(max_length=255, null=True)
    temperature = models.CharField(max_length=255, null=True)
    latt_cons = models.CharField(max_length=255, null=True)
    rerong = models.CharField(max_length=255, null=True)
    rpzxs = models.CharField(max_length=255, null=True)
    volume = models.CharField(max_length=255, null=True)
    density = models.CharField(max_length=255, null=True)
    energy = models.CharField(max_length=255, null=True)
    atomic_ener = models.CharField(max_length=255, null=True)
    form_ener = models.CharField(max_length=255, null=True)
    elastic_cons = models.CharField(max_length=255, null=True)
    wPoisson_rate = models.CharField(max_length=255, null=True)
    elasti_anis = models.CharField(max_length=255, null=True)
    wG_Ress = models.CharField(max_length=255, null=True)
    wK_Ress = models.CharField(max_length=255, null=True)
    mater_cate = models.CharField(max_length=255, null=True)
    brittle_tough = models.CharField(max_length=255, null=True)
    insert_time = models.DateTimeField(auto_now=True)
