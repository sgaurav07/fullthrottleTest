from django.db import models

# User model to store member details
class User(models.Model):
    real_name = models.CharField(max_length=100,null=False)
    tz = models.CharField(max_length=100)

    def __str__(self): 
        return str(self.real_name)

    class Meta:
        '''docstring for meta'''
        verbose_name_plural = "User Record"
    
#Activity model to store activity Period information
class Activity_Period(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.start_time)

    class Meta:
        '''docstring for meta'''
        verbose_name_plural = "Activity Period"
