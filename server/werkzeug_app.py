# Simple WSGI App using Werkzeug framework
# Importing Statements


# Request - A Werkzeug wrapper that provices an interface to access HTTP request data.
# Response  A Werkzeug wrapper used to create HTTP responses.
from werkzeug.wrappers import Request, Response
# A decorator that converts a function into a WSGI application
@ Request.application 


def application(request):
    # Prints clients IP Address
    print(f"This web server is running at {request.remote_addr}")
    return Response("A WSGI generated this response!")

# Main Block
if __name__ == "__main__":
    # run_simple - Werkzeug's simple WSGI server
    from werkzeug.serving import run_simple
    run_simple(
        #runs on localhost port 5555
        hostname="localhost",
        port=5555,
        # serves as WSGI Application
        application=application
    )