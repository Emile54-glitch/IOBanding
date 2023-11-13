from django.db import models

# Define your Band model which inherits from the 'models.Model' class.
class Band(models.Model):
    # Define a field to store the name of the band. It's a character field with a maximum length of 100 characters.
    name = models.CharField(max_length=100)
    
    # Define a field to store the description of the band. It's a text field for longer descriptions.
    description = models.TextField()
    
    # Define a field to store the number of members in the band. It's an integer field.
    members = models.IntegerField()

    # Define a human-readable representation of the model. This will be used in the Django admin interface.
    def __str__(self):
        return self.name  # Return the name of the band as its string representation.
