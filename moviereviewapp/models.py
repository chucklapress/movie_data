from django.db import models

# Create your models here
class Rater(models.Model):
    user_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=50)
    zipcode = models.CharField (max_length=10)

class Movie(models.Model):
    movie_id = models.IntegerField()
    movie_title = models.IntegerField()
    release_date = models.CharField(max_length=20)
    video_release_date= models.CharField(max_length=20)
    IMBd_URL = models.CharField(max_length=20)
    unknown = models.CharField(max_length=30)
    action = models.IntegerField()
    adventure = models.IntegerField()
    animation = models.IntegerField()
    childrens = models.IntegerField()
    comedy = models.IntegerField()
    crime = models.IntegerField()
    documentary = models.IntegerField()
    drama = models.IntegerField()
    fantasy = models.IntegerField()
    film_noir = models.IntegerField()
    horror = models.IntegerField()
    musical = models.IntegerField()
    mystery = models.IntegerField()
    romance = models.IntegerField()
    sci_fi = models.IntegerField()
    thriller = models.IntegerField()
    war = models.IntegerField()
    western= models.IntegerField()

class Review(models. Model):
    user_id = models.ForeignKey(Rater)
    movie_id = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()

    def __str__(self):
        return self.full_name









