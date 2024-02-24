from django.db import models

class DrugCategory(models.Model):
    ctgry_id = models.AutoField(primary_key=True)
    ctgry_nm = models.CharField(max_length=20)


class Drug(models.Model):
    drug_id = models.AutoField(primary_key=True)
    drug_nm = models.CharField(max_length=20)
    medical_use = models.CharField(max_length=200)
    title_image = models.URLField(max_length=200) # 대표 사진
    drug_type = models.CharField(max_length=200) # 
    ctgry = models.ForeignKey(DrugCategory, on_delete=models.CASCADE)

class DrugImage(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    image = models.URLField(max_length=200)

class DrugFeature(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    drug_feature = models.CharField(max_length=200)
    
class DrugAdr(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    adr_nm = models.CharField(max_length=225)

class UnintendedDrugUsage(models.Model):
    usage_id = models.AutoField(primary_key=True)
    usage_title = models.CharField(max_length=225)
    usage_ctnt = models.CharField(max_length=225)
    usage_image = models.URLField(max_length=225, default='')


