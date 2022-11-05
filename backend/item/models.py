from django.db import models

ITEM_CHANGE_CHOICES = [
    ("income", "in"),
    ("outgo", "out")
]


class Item(models.Model):
    name = models.CharField(max_length=70)
    manufacturer = models.CharField(max_length=70)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL())
    store = models.ForeignKey(Store, on_delete=models.SET_NULL())
    box = models.CharField(max_length=70)  # TODO: Change it to box in wherehouse
    unit = models.CharField()

    def __str__(self):
        return f"{self.name} {self.store} {self.manufacturer}"


class Store(models.Model):
    name = models.CharField(max_length=70)


class ItemChange(models.Model):
    name = models.ForeignKey(Item, on_delete=models.PROTECT())
    change = models.CharField(choices=ITEM_CHANGE_CHOICES, max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
