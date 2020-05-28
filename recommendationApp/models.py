from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name="Tag Id")
    name = models.TextField(verbose_name="Tag Name",null=False)
    description = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        indexes:[
            models.Index(fields=['name'],name='tag Index')
        ]
        constraints:[
            models.UniqueConstraint(fields=['name'],name="Unique Tag"),
        ]
    def __str__(self):
        return self.name

class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name="Video Id")
    name = models.TextField(verbose_name="Video Name",null=False, blank=False)
    path = models.TextField(verbose_name="File Path",null=True)
    videofile = models.FileField(upload_to='media/',null=False,verbose_name='Video File')
    created_on = models.DateTimeField(auto_now_add=True)
    thumbnail = models.TextField(verbose_name='thumnail')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    views = models.IntegerField(verbose_name="Video views",default=0)
    tags = models.ManyToManyField(Tag)
    class Meta:
        indexes:[
            models.Index(fields=['id'])
        ]

class Stats(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    video_views = models.IntegerField(verbose_name="Video views",default=0)
    interests = models.ManyToManyField(Tag)

class History(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    vid = models.ForeignKey(Video,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        indexes:[
            models.Index(fields=['uid','created_on'],name="history_search_index"),
            models.Index(fields=['uid'],name="user history index"),
            models.Index(fields=['vid'],name='video history index'),
        ]



# class VideTagRel(model.model):
#     vid = models.ForeignKey(Video,on_delete=models.CASCADE)
#     tig = models.ForeignKey(Tag,on_delete=models.CASCADE)
#     class Meta:
#         constraints:[
#             models.UniqueConstraint(fields=['vid','tig'])
#         ]
#         indexes:[
#             models.Index(fields=['vid']),
#             models.Index(fields=['tig']),
#             models.Index(fields=['vid','tig'])
#         ]



