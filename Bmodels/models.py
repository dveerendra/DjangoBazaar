from django.db import models

# Create your models here.
class UserInfo(models.Model):
    userName = models.CharField(max_length=128)
    eMailId = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    companyName = models.CharField(max_length = 255)
    address = models.TextField()
    role = models.IntegerField()   # We can define 0--student, 1 -- Teacher, and so on
    is_active = models.BooleanField()

    def __str__(self):
        return self.userName

class TokenGen(models.Model):
    Token = models.CharField(max_length=28)

class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner_org_name = models.CharField(max_length=255)
    license = models.CharField(max_length=255)
    free = models.BooleanField()
    link = models.TextField()
    itemType = models.CharField(max_length=32)   # trail, full version
    createdAt =  models.DateTimeField()
    lastModified = models.DateField()
    numberOfRatings = models.IntegerField()
    numberOfLikes = models.IntegerField()
    author = models.ForeignKey(UserInfo)

    def __str__(self):
        return self.title

    def getLikesOfItem(self):
        return self.numberOfLikes

    #def RecentelyCreatedItems():

    #def MostLikedItems(self, asd):
        #s = asd;

class Tags(models.Model):
    name= models.CharField(max_length=128)
    createdAt = models.DateTimeField()
    lastModified = models.DateTimeField()
    author = models.ForeignKey(UserInfo,related_name='user_id')
    lastModifiedBy = models.ForeignKey(UserInfo,related_name='modified_by_user_id')

    def __str__(self):
        return self.Name

class ItemTags(models.Model):
    itemId = models.ForeignKey(Item)
    tagsId = models.ForeignKey(Tags)



class Ratings(models.Model):
    rate = models.IntegerField()
    comments = models.TextField()
    createdAt = models.DateTimeField()
    author= models.ForeignKey(UserInfo)

    def __str__(self):
        return  self.Rate

class ItemRatings(models.Model):
    itemId = models.ForeignKey(Item)
    ratingsID = models.ForeignKey(Ratings)