# views.py
__author__ = 'robertv'
__copyright__ = "QED Testing, Inc. 2013"

from Common.view_helpers import render_template


def about(request):
    debug_text = " Language:" + request.LANGUAGE_CODE + ":"
    action_template = "General/About_CB.htm"
    return render_action_template(request, locals())


def render_action_template(request, p_locals):
    return render_template(request, 'CaracalHomePage.html', p_locals)