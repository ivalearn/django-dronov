from django.db import models


class Category(models.Model):
    class Meta:
        ordering = ("name",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Good(models.Model):
    class Meta:
        ordering = ("-price", "name")
        unique_together = ("category", "name", "price")
        verbose_name = "товар"
        verbose_name_plural = "товары"
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")
    description = models.TextField()
    price = models.FloatField()
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name="В наличии")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def get_is_stock(self):
        if self.in_stock:
            return "+"
        else:
            return ""

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s += " (нет в наличии)"
        return s
