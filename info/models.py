from django.db import models

# Create your models here.

class Musician(models.Model):
    #id = models.AutoField(Primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    ratings = (
        (1, "Worst"),
        (2, "Bad"),
        (3, "Not bad"),
        (4, "Good"),
        (5, "Excellent"),
    )

    num_stars = models.IntegerField(choices=ratings)

    def __str__(self):
        return self.name + ", " + "Ratings: " + str(self.num_stars)