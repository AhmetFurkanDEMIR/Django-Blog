from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):

    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yayınlanma Tarihi")
    article_image = models.FileField(blank=True, null=True, verbose_name="makale fotoğrafı")

    def __str__(self) -> str:
        return self.title

    