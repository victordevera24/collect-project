from django.db import models

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Fish(models.Model):
    name = models.CharField(max_length=100)
    size = models.FloatField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta: 
        ordering = ['-date']