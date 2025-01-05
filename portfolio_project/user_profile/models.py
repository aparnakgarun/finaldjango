from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    work_experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectShowcase(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project_name
