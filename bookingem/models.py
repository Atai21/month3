from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text
