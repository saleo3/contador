# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

tit = 'Contador de visitas'

def index():
    if not session.counter:
        session.counter = 1
    else:
        session.counter += 1
    return dict(nv=session.counter,titulo=tit)
