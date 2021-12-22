from es import ElasticSearchClient
from mysql import MysqlClient


class Database(object):
    def factory(object_type, **kwargs):
        if object_type == "ES":
            return ElasticSearchClient(**kwargs)
        if object_type == "MySQL":
            return MysqlClient()
        assert 0, "Bad request: " + object_type

    factory = staticmethod(factory)
