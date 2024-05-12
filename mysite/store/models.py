from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Tool(models.Model):
    tags = TaggableManager()

    class Provider(models.TextChoices):
        TH_TOOLS = 'TH', 'th-tool.by'
        TT_TOOLS = 'TT', 'www.store.by'
        ARMTEK = 'AR', 'etp.armtek.by'
        HOREX = 'HR', 'gammatest.by'
        FORCE = 'FR', 'Force-Yato'
        STAB = 'ST', 'kubala.by'

    code = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    brand = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=600)
    note = models.TextField(blank=True, max_length=600)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    provider = models.CharField(max_length=2, choices=Provider.choices)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:tool_detail',
                       args=[self.id])
