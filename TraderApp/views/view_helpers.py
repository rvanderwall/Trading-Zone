__author__ = 'robertv'

import datetime
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

def requires_login(view):
    authorized = True
    def new_view(request, *args, **kwargs):
        if not authorized:
            return HttpResponseRedirect('/login/')
        return view(request, *args, **kwargs)
    return new_view


# Renders a page using the action_template and current_section defined in locals()
# Renders through the Home page
def render_action_template(request, p_locals):
    return render_template(request, 'TraderHomePage.html', p_locals)

# Same as render_action_template except you specify the home page.
# Good for registration and such where you want a clean page
def render_template(request, template_name, p_locals):
    current_date = datetime.datetime.now()
    user = request.user
    c = locals()
    c.update(csrf(request))
    c.update(p_locals)
    return render_to_response(template_name, c)
