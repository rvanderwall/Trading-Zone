__author__ = 'robertv'

from django.utils.translation import ugettext_noop, ugettext_lazy as _

# Strings for Models
help_name = _('Full name of user, denormalized with User')
help_address = _("Street Address")

# Strings for Registration page
label_email = _("Email")
invalid_email = _("Must be valid email address, less that 30 characters.")
help_email = _("Required. Must be valid email address")

# Not translated in the DB, they may get translated when displayed to user
default_address = ugettext_noop("No Address provided")
default_city = ugettext_noop("No City provided")
default_state = ugettext_noop("No State provided")


# Strings for Hunt page
label_hunt_words = _("Keywords for your hunt")
invalid_hunt_words = _("Please use less than 6 words to hunt.")
mail_subject = _("Hello %(name)s, I'm interested in the item you have for sale.")
mail_body = _("%(intro)s\nPlease let me know if it's still available.\nThanks")

# String for Sell page
invalid_price = _("Please enter a valid price, like 150.00.")


# System wide strings
invalid_not_logged_in = _("You are not logged in")

# Strings for the title
section_about = _("About")
section_show_items = _("Show Items For Sale")
section_show_details = _("Show Item details")
section_sell_item = _("Sell an Item")
section_add_hunt = _("Add a search request")
section_registration_compete = _("Registration Complete")