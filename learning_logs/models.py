"""
18-2. 
Short Entries: The __str__() method in the Entry model currently appends
an ellipsis to every instance of Entry when Django shows it in the admin site
or the shell. Add an if statement to the __str__() method that adds an ellipsis
(continued)
Getting Started with Django
387only if the entry is longer than 50 characters. Use the admin site to add an
entry that’s fewer than 50 characters in length, and check that it doesn’t have
an ellipsis when viewed.
"""


from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """ A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """ Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """ Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """ Return a simple string representing the entry."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text


# from django.db import models

# # Create your models here.

# class Topic(models.Model):
#     """ A topic the user is learning about."""
#     text = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         """ Return a string representation of the model."""
#         return self.text

# class Entry(models.Model):
#     """ Something specific learned about a topic."""
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'entries'

#     def __str__(self):
#         """ Return a simple string representing the entry."""
#         return f"{self.text[:50]}..."
    