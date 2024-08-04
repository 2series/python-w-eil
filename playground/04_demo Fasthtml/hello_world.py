# script a simple web application written in Python using the FastHTML framework


# Importing modules
from fasthtml.common import *

# Create app
# app = FastHTML()

# Defining a route
# @app.get('/')
# def get():
#     return P('Hello, World!')

# Serving the aoo
# serve()


# script a simple web application written in Python using the FastHTML framework

# Create app
app = FastHTML()

# Defining a route for the home page
@app.get('/')
def home():
    return H1('Welcome to My App'), P('This is a simple web application built with FastHTML.')

# Serving the app
serve()