from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils.urlutils import admin_reverse
from polls.models import Poll


@toolbar_pool.register
class PollToolbar(CMSToolbar):
    
    watch_models = [Poll,]

    def populate(self):
        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu('poll-app', _('Polls'))

        menu.add_sideframe_item(
            name=_('Poll list'),
            url=admin_reverse('polls_poll_changelist'),
        )

        menu.add_modal_item(
            name=_('Add new poll'),
            url=admin_reverse('polls_poll_add'),
        )
