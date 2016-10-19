from cms.models.pluginmodel import CMSPlugin

from django.db import models

class MaxEntries(CMSPlugin):
  max_entries = models.SmallIntegerField(default=0, verbose_name='Maximum Entries')
  