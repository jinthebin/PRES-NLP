from functools import wraps
from flask import session, redirect, url_for
'''
Author: Abhinav Jindal

Added basic authentication based on a single user credential

This has replaced flask's implementation of basic auth using make_response
& request

'''

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Check if the user has a valid session
        if not session.get('is_logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated


# from functools import wraps
# from flask import make_response, request

# def auth_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#         if auth and auth.username == "user1" and auth.password == "pass":
#             return f(*args, **kwargs)
#         return make_response("<h1>Access denied.</h1>", 401, 
#                              {'WWW-Authenticate': 'Basic realm="Login required!"'})
#     return decorated