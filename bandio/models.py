# models.py
from django.db import models

class Band(models.Model):
    """
    Model representing a music band.
    """
    name = models.CharField(max_length=100, help_text="Enter the name of the band.")
    description = models.TextField(help_text="Enter a description for the band.")
    members = models.IntegerField(help_text="Enter the number of members in the band.")

    def __str__(self):
        """
        String representation of the Band object.
        """
        return self.name
