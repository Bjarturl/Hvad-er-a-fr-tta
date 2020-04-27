# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Allnewsarticles(models.Model):
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=255, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    month = models.FloatField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    year = models.FloatField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    newsimagelink = models.CharField(db_column='NewsImageLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imagecaption = models.CharField(db_column='ImageCaption', max_length=255, blank=True, null=True)  # Field name made lowercase.
    page = models.CharField(db_column='Page', max_length=255, blank=True, null=True)  # Field name made lowercase.
    article = models.TextField(db_column='Article', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AllNewsArticles'