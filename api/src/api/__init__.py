from sanic import Blueprint

from api.v1 import v1

api = Blueprint.group(v1, version_prefix='/v')