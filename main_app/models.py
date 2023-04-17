from django.db import models
from django.urls import reverse

# Create your models here.
MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner'),
)

class Finch(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    age = models.IntegerField

    def __str__(self):
      return f'{self.name} ({self.id})'

    def get_absolute_url(self):
     return reverse('detail', kwargs={'finch_id': self.id})
    
   
class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField( max_length=1,
    choices=MEALS,
    default=MEALS[0][0])
  
finch = models.ForeignKey(
    Finch,
    on_delete=models.CASCADE
  )
  
def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  # Create a cat_id FK
  finch = models.ForeignKey(
    Finch,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

