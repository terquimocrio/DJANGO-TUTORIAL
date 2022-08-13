from turtle import title
from django.db import models

# Create your models here.
class Book(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100, verbose_name="Title")
  image = models.ImageField(upload_to="images/", verbose_name="Image", null=True)
  description = models.TextField(verbose_name="Descriprion",null=True)

  def __str__(self) -> str:
    row = "Title: " + self.title + " - " + "Description: " + self.description
    return row

  def delete(self, using=None, keep_parents=False):
    self.image.storage.delete(self.image.name)
    super().delete()