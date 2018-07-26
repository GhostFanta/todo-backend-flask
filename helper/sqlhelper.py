from sqlalchemy.ext.declarative import DeclarativeMeta
import json


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


def kt2dict(keyed_tuple):
    """ sqlalchemy.util._collections.KeyedTuple to dict """
    return dict(zip(keyed_tuple.keys(), keyed_tuple))


def sqla2dict(model):
    """ Declarative Base model to dict """
    print(model.__table__.columns)
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}
