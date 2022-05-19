from django.db import models


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.name
        
# Create your models here.
class Fish(models.Model):
    name = models.CharField(max_length=100)
    size = models.FloatField(max_length=100)
    description = models.TextField(max_length=250)

    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

class Photo(models.Model):
    url = models.CharField(max_length=200)
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for fish_id: {self.fish_id} @{self.url}"


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
