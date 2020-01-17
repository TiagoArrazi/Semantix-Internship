from flask import Flask
from flasgger import Swagger
from glob import glob
from importlib import import_module
from os.path import join, dirname, basename


app = Flask(__name__)


template = {
    "title": "Hello World",
    "swagger": "2.0",
    "info": {
        "title": "Hello World",
        "description": "API de teste com retorno clássico 'Hello World!'",

    }
}

swagger = Swagger(app, template=template)

modules = glob(join(dirname(__file__), "../docs/definitions/*.py"))
module_names = [import_module("{}.{}".format("docs.definitions", basename(f)[:-3]))
        for f in modules if isfile(f) and not f.endswith("__init__.py")]
