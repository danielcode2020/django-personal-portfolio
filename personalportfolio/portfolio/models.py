from django.db import models

from django.db import models

class CVSection(models.Model):
    header = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField(unique=True, help_text="Numărul de ordine pentru aranjare")

    class Meta:
        ordering = ['order'] # Asigură sortarea implicită după numărul de ordine

    def __str__(self):
        return f"{self.order}. {self.header}"