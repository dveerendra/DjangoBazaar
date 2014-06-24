from django.db import models
from django.contrib.auth.models import User, Group
import datetime
# Create your models here.

# We should probably use Django's own User Model. Has almost
# all the info defined here:
"""
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
"""

# If this is meant to generate tokens for OAuth2 used in API, the rest-framework
# will provide generator.
"""
class TokenGen(models.Model):ss
    Token = models.CharField(max_length=28)
"""

#Collection information is stored in this table
class MaterialCollections(models.Model):
    cTitle = models.CharField(max_length=255)
    createdAt =  models.DateTimeField(auto_now_add=True)
    lastModified = models.DateField(auto_now_add=True)

class hasCollection(models.Model):
    parentID = models.ForeignKey(MaterialCollections)
    childID = models.ForeignKey(MaterialCollections)

# fill in all the details we created for the API-definition
# and discuss the rating-thumb thing
class MaterialItem(models.Model):
    mTitle = models.CharField(max_length=255)
    description = models.TextField(max_length=8000)
    owner_org_name = models.CharField(max_length=255)   #this might be foreignkey
    license = models.CharField(max_length=255)
    free = models.BooleanField(default=True)
    link = models.TextField(max_length=8000)
    itemType = models.CharField(max_length=32)   # trial, full version
    createdAt =  models.DateTimeField(auto_now_add=True)
    lastModified = models.DateField(auto_now_add=True)
    numberOfRatings = models.IntegerField(default=0)
    numberOfLikes = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    collectionId = models.ForeignKey(MaterialCollections)

    def __str__(self):
        return self.title

    def getLikesOfItem(self):
        return self.numberOfLikes


# this is folksonomical tag right?
# needs modifications to be usable with Django's own user-system
class Tags(models.Model):
    name = models.CharField(max_length=128)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,related_name='user_id')
    lastModifiedBy = models.ForeignKey(User,related_name='modified_by_user_id')
    ItemTags = models.ManyToManyField(MaterialItem)

    def __str__(self):
        return self.Name


#class ItemTags(models.Model):
 #   itemId = models.ForeignKey(MaterialItem)
  #  tagsId = models.ForeignKey(Tags)


#note the separation of the comments and ratings:
class Ratings(models.Model):
    rate = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User)

    def __str__(self):
        return self.Rate

class ItemRatings(models.Model):
    itemId = models.ForeignKey(MaterialItem)
    ratingsID = models.ForeignKey(Ratings)


class Comment(models.Model):
    commentText = models.TextField(max_length=8000)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.commentText

class ItemComments(models.Model):
    itemId = models.ForeignKey(MaterialItem)
    commentsID = models.ForeignKey(Comment)

#
class ProviderOrganization(models.Model):
    organizationName = models.CharField(max_length=2000)
    ownerUser = models.ForeignKey(User) #foreign key to the User (CMS user-account)

#connects the material to the owner organization
class ownerOfMaterial(models.Model):
    itemId = models.ForeignKey(MaterialItem)
    organizationId = models.ForeignKey(ProviderOrganization)
