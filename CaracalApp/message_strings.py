# admin.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

from django.utils.translation import ugettext_noop, ugettext_lazy as _

# Strings for Models
help_name = _('Full name of user, denormalized with User')
help_address = _("Street Address")


# Strings for Hunt page
label_hunt_words = _("Keywords for your hunt")
invalid_hunt_words = _("Please use less than 6 words to hunt.")
mail_subject = _("Hello %(name)s, I'm interested in the item you have for sale.")
mail_body = _("%(intro)s\nPlease let me know if it's still available.\nThanks")

# String for Sell page
invalid_price = _("Please enter a valid price, like 150.00.")


# Strings for the title
section_about = _("About")
section_show_items = _("Show Items For Sale")
section_show_details = _("Show Item details")
section_sell_item = _("Sell an Item")
section_add_hunt = _("Add a search request")
