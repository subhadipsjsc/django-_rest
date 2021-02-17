from django.db import models

# Create your models here.
class ArtifactModel(models.Model) :
    name = models.CharField(max_length=100)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.name