# message_strings.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

from django.utils.translation import ugettext_noop, ugettext_lazy as _

# Not translated in the DB, they may get translated when displayed to user
default_address = ugettext_noop("No Address provided")
default_city = ugettext_noop("No City provided")
default_state = ugettext_noop("No State provided")

# Strings for Registration page
label_email = _("Email")
invalid_email = _("Must be valid email address, less that 30 characters.")
help_email = _("Required. Must be valid email address")

# System wide strings
invalid_not_logged_in = _("You are not logged in")

# Strings for the title
section_registration_compete = _("Registration Complete")