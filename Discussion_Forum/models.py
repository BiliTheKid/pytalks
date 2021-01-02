from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# parent model
class forum(models.Model):
    name = models.CharField(max_length=200, default="anonymous")
    email = models.CharField(max_length=200, null=True)
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)
    link = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.topic)


# child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.forum)

################################################
class Status(models.Model):
    """"
    status for thread,post..lock,unlock
    """
    status_id = models.IntegerField(default=0, blank=True,
                                    editable=False, help_text='status id') # pk
    status_name = models.CharField(max_length=30,help_text='status name')

    def __str__(self):
        return self.status_name

class UserStatus(models.Model):
    """"
    user status
    """
    status_id = models.IntegerField(default=0, blank=True, editable=False) #pk
    status_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.status_name


class User(models.Model):
    user_id = models.IntegerField(primary_key=True) #pk
    user_name = models.CharField(max_length=1000)
    user_email = models.CharField(max_length=50)
    user_pass = models.CharField(max_length=50)
    user_created = models.DateTimeField(auto_now_add=True)
    user_status = models.ForeignKey(UserStatus, blank=True, on_delete=models.CASCADE)


    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of the model."""
    #     return reverse('model-User-view', args=[str(self.user_id)])

    def __str__(self):
        return self.user_name


class ThreadForum(models.Model):
    Thread_forum_id = models.IntegerField(primary_key=True,default='') #pk
    Thread_forum_subject = models.CharField(max_length=1000,default='')
    Thread_forum_created = models.DateTimeField(auto_now_add=True)
    Thread_forum_user_id = models.ForeignKey(User, blank=True, on_delete=models.CASCADE,default='') #fk
    status = models.ForeignKey(Status, blank=True, on_delete=models.CASCADE,default='')



    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-Thread Forum-view', args=[str(self.Thread_forum_id)])

    def __str__(self):
        return self.Thread_forum_subject







class Post(models.Model):
    post_id = models.IntegerField(primary_key=True) # pk
    #post_title = models.CharField(max_length=1000)
    post_created = models.DateTimeField(auto_now_add=True)
    post_content = models.CharField(max_length=1000)
    post_user_id = models.ForeignKey(User, blank=True, on_delete=models.CASCADE) # fk
    post_thread_id = models.ForeignKey(ThreadForum, blank=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, blank=True, on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of the model."""
    #     return reverse('model-post-view', args=[str(self.post_id)])

    def __str__(self):
        return self.post_content

class Vote(models.Model):
    vote_id = models.IntegerField(primary_key=True)
    vote_up_count = models.IntegerField(blank=True, null=True)
    vote_down_count = models.IntegerField(blank=True, null=True)
    vote_thread_id = models.ForeignKey(ThreadForum, blank=True, on_delete=models.CASCADE)
    vote_post_id = models.ForeignKey(Post, blank=True, on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of the model."""
    #     return reverse('model-Vote-view', args=[str(self.vote_id)])

    def __str__(self):
        return self.vote_id

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=1000)
    category_description = models.CharField(max_length=1000)
    creator = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status_id = models.ForeignKey(Status, blank=True, on_delete=models.CASCADE)
    #number_category_id = models.ForeignKey(category_id, blank=True, on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of the model."""
    #     return reverse('model-User-view', args=[str(self.category_id)])

    def __str__(self):
        return self.category_name


class Group(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=1000)
    category_id = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    user_group_id = models.IntegerField(blank=True, null=True)
    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of the model."""
    #     return reverse('model-User-view', args=[str(self.group_name)])

    def __str__(self):
        return self.group_name

class UserGroup(models.Model):
    user_id = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, blank=True, on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of the model."""
    #     return reverse('model-User-view', args=[str(self.group_id)])

    def __str__(self):
        return self.group_id



