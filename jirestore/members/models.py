from django.db import models
from django.urls import reverse

class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  
class Author(models.Model):
             
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
      
    class Meta:
        ordering = ['last_name', 'first_name']
        
    def get_absolute_url(self):
      return reverse('author-detail', args=[str(self.id)])

    def __str__(self):  
      return f'{self.last_name}, {self.first_name}'
