from django.db import models


class users(models.Model):
    id = models.CharField(primary_key=True,max_length=255)

    name = models.CharField(max_length=255)

    phone = models.CharField(max_length=11)

    password = models.CharField(max_length=500)
    user_type = models.BooleanField(default=False)
    


class cinema_house(models.Model):
    id = models.CharField(primary_key=True,max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    disc = models.CharField(max_length=255)
    no_of_rooms = models.IntegerField()



class movies(models.Model):
    name = models.CharField(max_length=255)
    id = models.CharField(primary_key=True,max_length=255)

class movie_price_cinema(models.Model):
    id = models.CharField(primary_key=True,max_length=255)
    movie = models.ForeignKey("movies",on_delete=models.CASCADE,null=True)
    cinema = models.ForeignKey("cinema_house",on_delete=models.CASCADE,null=True)
    price = models.IntegerField()
    
class ticket(models.Model):
    id = models.CharField(primary_key=True,max_length=255)
    user = models.ForeignKey("users", on_delete=models.CASCADE,null=True)
    movie = models.ForeignKey("movies",on_delete=models.CASCADE,null=True)
    cinema = models.ForeignKey("cinema_house",on_delete=models.CASCADE,null=True)
    price = models.ForeignKey("movie_price_cinema",on_delete=models.CASCADE,null=True)