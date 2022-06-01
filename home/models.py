from django.db import models

# Create your models here.
class Microsection(models.Model):
    CAD_NO = models.CharField(max_length=122)
    MANUFACTURER_NAME = models.CharField(max_length=122)
    PANEL_NO = models.CharField(max_length=122)
    DATE_CODE = models.CharField(max_length=122)
    PCB_SI_NOS = models.CharField(max_length=122)
    PCB_THICKNESS = models.CharField(max_length=122)
    LAYER_COUNT = models.CharField(max_length=122)
    PROJECT = models.CharField(max_length=122)
    APPLIED_SERIAL_NOS = models.CharField(max_length=122)
    TESTING_AGENCY = models.CharField(max_length=122)
    Load_day = models.CharField(max_length=122)
    Load_Month = models.CharField(max_length=122)
    Load_Year = models.CharField(max_length=122)
    Result_day = models.CharField(max_length=122)
    Result_Month = models.CharField(max_length=122)
    Result_Year = models.CharField(max_length=122)
    Receipt_Day = models.CharField(max_length=122)
    Receipt_Month = models.CharField(max_length=122)
    Receipt_Year = models.CharField(max_length=122)
    Result = models.CharField(max_length=122)
    # REMARK = models.CharField(max_length=122)

    def __str__(self):
        return self.CAD_NO
        return self.MANUFACTURER_NAME
        return self.PANEL_NO
        return self.DATE_CODE
        return self.PCB_SI_NOS
        return self.PCB_THICKNESS
        return self.LAYER_COUNT
        return self.PROJECT
        return self.APPLIED_SERIAL_NOS
        return self.TESTING_AGENCY
        return self.Load_day
        return self.Load_Month
        return self.Load_Year
        return self.Result_day
        return self.Result_Month
        return self.Result_Year
        return self.Receipt_Day
        return self.Receipt_Month
        return self.Receipt_Year
        return self.Result
        # return self.REMARK