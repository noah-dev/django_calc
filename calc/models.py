from django.db import models

# Create your models here.


class calc_log(models.Model):
    op_a = models.FloatField(null=True)
    op = models.CharField(max_length=200, null=True)
    op_b = models.FloatField(null=True)
    res = models.FloatField(null=True)
    calc_time = models.DateTimeField('date published')

    def __str__(self):
        return str(self.op_a) + " " + self.op + " " + str(self.op_b) +\
            " = " + str(self.res) + " | Time: " + str(self.calc_time)
