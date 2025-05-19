from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    message = models.TextField()
    date = models.DateField(db_index=True, auto_now_add=True)
    idEscritor = models.ForeignKey(
    'users.CustomUser',  # AppName.ModelName
    on_delete=models.CASCADE
    
)
    active = models.BooleanField(default=True)
    

# Create your models here.
