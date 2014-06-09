from django.db import models

# Create your models here.
class UserInfo(models.Model):
    UserName = models.CharField(max_length=128)
    EMailId = models.CharField(max_length = 255)
    Password = models.CharField(max_length = 255)
    CompanyName = models.CharField(max_length = 255)
    Address = models.TextField()
    Role = models.IntegerField()   # We can define 0--student, 1 -- Teacher, and so on
    is_active = models.BooleanField()

    def __str__(self):
        return self.UserName

class Item(models.Model):
    Title = models.CharField(max_length=255)
    Description = models.TextField()
    Owner_org_name = models.CharField(max_length=255)
    License = models.CharField(max_length=255)
    Free = models.BooleanField()
    Link = models.TextField()
    type = models.CharField(max_length=32)   # trail, full version
    CreatedAt =  models.DateTimeField()
    LastModified = models.DateField()
    NumberOfRatings = models.IntegerField()
    NumberOfLikes = models.IntegerField()
    Author = models.ForeignKey(UserInfo)

    def __str__(self):
        return self.Title

    def getLikesOfItem(self):
        return self.NumberOfLikes

    #def RecentelyCreatedItems():

    #def MostLikedItems(self, asd):
        #s = asd;

class Tags(models.Model):
    Name= models.CharField(max_length=128)
    CreatedAt = models.DateTimeField()
    LastModified = models.DateTimeField()
    Author = models.ForeignKey(UserInfo,related_name='user_id')
    LastModifiedBy = models.ForeignKey(UserInfo,related_name='modified_by_user_id')

    def __str__(self):
        return self.Name

class ItemTags(models.Model):
    ItemId = models.ForeignKey(Item)
    TagsId = models.ForeignKey(Tags)



class Ratings(models.Model):
    Rate = models.IntegerField()
    Comments = models.TextField()
    CreatedAt = models.DateTimeField()
    Author= models.ForeignKey(UserInfo)

    def __str__(self):
        return  self.Rate

class ItemRatings(models.Model):
    ItemId = models.ForeignKey(Item)
    RatingsID = models.ForeignKey(Ratings)