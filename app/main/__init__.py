from flask import Blueprint

main = Blueprint('main', __name__)

#Blueprints are created by instantiating an object of class Blueprint. The constructor for this class takes two required arguments: the blueprint name and the module or package where the blueprint is located. As with applications, Python’s __name__ variable is in most cases the correct value for the second argument.

from . import views, errors