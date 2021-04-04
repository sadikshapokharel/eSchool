from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.
class Banner(models.Model):
    image = models.ImageField()

class Semester(models.Model):
    semester_name = models.CharField(max_length=100)
    image = models.ImageField()
    def __str__(self):
        return self.semester_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    credit_hour = models.IntegerField()
    image = models.ImageField()
    semester_name = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name
    
class Chapter(models.Model):
    chapter_title = models.CharField(max_length=100)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.chapter_title

class Resource(models.Model):
    chapter_title = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    notes = models.FileField(upload_to='notes')
    video_url = EmbedVideoField()
    
    