import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from buedastatus.lib.base import BaseController, render
from buedastatus.lib.check import is_bueda_up
from buedastatus.model.meta import Session
from buedastatus.model.status import Status

log = logging.getLogger(__name__)

class StatusController(BaseController):

    def index(self):
        # Return a rendered template
        c.statuses = Session.query(Status).order_by('time').limit(25)
        return render('/status.mako')

    def check(self):
        status = ("Ok" if is_bueda_up() else "Not Ok")
        status = Status(status=status)
        Session.add(status)
        Session.commit()
        return status.status

        
