from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from myblog.models import Category, CategoryExtension
from cms.models import Title

from .models import MaxEntries

class MenuPlugin(CMSPluginBase):
    model = MaxEntries
    name = _("Menu Plugin")
    render_template = "menu_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
      blogposts = []
      for t in Title.objects.all():
        if t.page.publisher_is_draft==False:
          try:
            if str(t.page.categoryextension.category) == 'post':
              anchor = (t.title,t.path)
              blogposts.append(anchor)
          except:
            pass
            
      context['instance'] = instance  
      context['blogposts'] = blogposts
      return context

plugin_pool.register_plugin(MenuPlugin)