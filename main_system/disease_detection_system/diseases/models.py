from pyexpat import model
from django.db import models

# Create your models here.
class Heart(models.Model):
    age=models.PositiveIntegerField()
    
    MALE = '1'
    FEMALE = '0'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default=MALE
    )
    cp=models.PositiveSmallIntegerField()
    trestbps=models.PositiveIntegerField()
    chol=models.PositiveIntegerField()
    GT_120 = '1'
    LT_120 = '0'
    FBS_CHOICES = (
        (GT_120, '>120'),
        (LT_120, '<120'),
    )

    fbs = models.CharField(
        max_length=1,
        choices=FBS_CHOICES,
        default=MALE
    )
    restecg=models.SmallIntegerField()
    thalach=models.SmallIntegerField()
    exang=models.SmallIntegerField()
    oldpeak=models.SmallIntegerField()
    slope=models.SmallIntegerField()
    ca=models.SmallIntegerField()
    thal=models.SmallIntegerField()
    target=models.SmallIntegerField()

class Kidney(models.Model):
    age=models.SmallIntegerField()
    bp=models.SmallIntegerField()
    sg=models.FloatField()
    al=models.SmallIntegerField()
    su=models.SmallIntegerField()
    rbc=models.BooleanField()
    pc=models.BooleanField()
    pcc=models.BooleanField()
    ba=models.BooleanField()
    bgr=models.BooleanField()
    bu=models.SmallIntegerField()
    sc=models.FloatField()
    sod=models.SmallIntegerField()
    hemo=models.FloatField()
    pcv=models.SmallIntegerField()

class Liver(models.Model):
    age=models.SmallIntegerField()
    gender=models.BooleanField()
    total_bilirubin=models.FloatField()
    direct_bilirubin=models.FloatField()
    alkaline_phosphotase=models.SmallIntegerField()
    alamine_amino=models.SmallIntegerField()
    total_proteins=models.SmallIntegerField()
    albumin=models.FloatField()
    albuumin_and_glubin_ratio=models.FloatField()

