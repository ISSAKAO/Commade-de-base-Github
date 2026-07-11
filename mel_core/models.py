from django.db import models

class SGC(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.country})"

class Project(models.Model):
    sgc = models.ForeignKey(SGC, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Indicator(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class IndicatorValue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='indicator_values')
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE, related_name='values')
    value = models.FloatField()
    date_recorded = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.indicator.name} - {self.project.title}: {self.value}"
