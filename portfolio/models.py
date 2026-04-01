from django.db import models

from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    # The default 'fas fa-code' ensures an icon shows even if you forget to add one
    icon_class = models.CharField(
        max_length=100,
        default="fas fa-code",
        help_text="Enter FontAwesome class (e.g., 'fab fa-python', 'fas fa-database')"
    )

    def __str__(self):
        return self.name


class Education(models.Model):
    university = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    year_attended = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.degree} at {self.university}"


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # upload_to creates a folder automatically inside 'media'
    picture = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title