from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class NewWord(models.Model):
    id = models.BigAutoField(primary_key=True)
    word = models.CharField(unique=True,max_length=20)
    explain = models.TextField(blank=False)
    #through_fields=('user_id')
    like_user_ids = models.ManyToManyField(User ,related_name='likeword', blank=True, through='NewWord_user')
    create_time = models.DateTimeField(auto_now_add=True) 
    create_user_id = models.ForeignKey(User, to_field='username', related_name = "newword", on_delete=models.CASCADE,db_column="create_user_id")
    likeCnt = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.word)

class NewWord_user(models.Model):
    user_id=models.ForeignKey(User, to_field='username' ,on_delete=models.CASCADE,db_column="user_id", primary_key=True)
    Newword_id=models.ForeignKey('Newword' ,on_delete=models.CASCADE,db_column="post_id", null=True)
    class Meta:
        db_table="NewWord_user"