import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to
from sqlalchemy import desc

from buedastatus.lib.base import BaseController, render
from buedastatus.lib.check import is_bueda_up
from buedastatus.model.meta import Session
from buedastatus.model.status import Status

log = logging.getLogger(__name__)
PER_PAGE = 100

class StatusController(BaseController):

    def index(self):
        # Return a rendered template
        c.statuses = Session.query(Status).order_by(desc(Status.time)).limit(PER_PAGE)
        c.page = 1
        return render('/status.mako')

    def page(self, page):
        # Return a rendered template
        c.page = int(page)
        page = c.page - 1
        c.statuses = Session.query(Status).order_by(desc(Status.time)).offset(PER_PAGE * page).limit(PER_PAGE)
        return render('/status.mako')

    def check(self):
        status = ("Ok" if is_bueda_up() else "Not Ok")
        status = Status(status=status)
        Session.add(status)
        Session.commit()
        return status.status

        
