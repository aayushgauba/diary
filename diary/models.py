from django.db import models

class DiaryEntry(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f"Entry for {self.date}"