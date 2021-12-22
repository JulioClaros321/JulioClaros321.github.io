import uuid
from copy import deepcopy

import elasticsearch

from Database.es.es_utils import is_empty

MAX_SIZE = 1000
SIZE = 10000
REQUEST_TIMEOUT = 300


def make_query(search_array=None, filter_array=None, to_return='*', count_query='yes'):
    """
    searchArray is of the format : [
                                    ["toSearchFor", "fields, *to, search^3, in*" ],
                                    ["toSearchFor2", ...],
                                    ...
                            ]
    filterArray is of the format : [
                                    ["toSearchFor", "fields, *to, search^3, in*" ],
                                    ["field_to_filter_on", min_value, max_value],
                                    ...
                            ]
    toReturn is an array of fields to be returned in the results
    """
    if search_array is None:
        search_array = []
    if filter_array is None:
        filter_array = []
    query_must_array = []

    for one_s in search_array:
        if one_s[1] == '*':
            fields = '*'
        else:
            fields = one_s[1].split(',')
        search_dict = {
            'multi_match': {
                'query': one_s[0],
                'type': 'phrase',
                'fields': fields
            }
        }
        query_must_array.append(search_dict)

    for values in filter_array:
        search_dict = dict()
        if len(values) == 3:
            search_dict = {
                'range': {
                    values[0]: {
                        'gte': values[1],
                        'lte': values[2]
                    }
                }
            }
        elif len(values) == 2:
            if values[1] == '*':
                fields = '*'
            else:
                fields = values[1].split(',')
            search_dict = {
                'multi_match': {
                    'query': values[0],
                    'type': 'phrase',
                    'fields': fields
                }
            }
        filter_array.append(search_dict)

    if count_query == 'yes':

        query = {
            'query': {
                'bool': {
                    'must': query_must_array,
                    'filter': filter_array
                }
            },
            '_source': to_return
        }
    else:
        query = {
            'query': {
                'bool': {
                    'must': query_must_array,
                    'filter': filter_array
                }
            }
        }
    return query


class ElasticSearchClient:

    def __init__(self,es_url="elasticsearch", es_port="8001", **kwargs):
        self._ES_URL = es_url
        self._ES_PORT = es_port
        if kwargs is not None:
            try:
                self._PRE_PROCESS_HARD = kwargs.get('preprochard')
                self._SEARCHES = kwargs.get('searches')
                self._USERS = kwargs.get('users')
                self._EQUILATERAL = kwargs.get('equilateral')
                self._MERCURIAL = kwargs.get('mercurial')
            except Exception as e:
                raise e

    def get_es_connection(self):
        try:
            es_connection = elasticsearch.Elasticsearch([{'host': self._ES_URL, 'port': self._ES_PORT}])
        except Exception as e:
            raise e
        return es_connection

    def nested_es_search(self, es_query=None, size=200):
        if is_empty(es_query):
            return "Empty query"

        es_connection = self.get_es_connection()
        try:
            res = es_connection.search(index=self._PRE_PROCESS_HARD, size=size, body=es_query, request_timeout=300)
            res = [r['_source'] for r in res['hits']['hits']]
        except Exception:
            raise
        return res

    def search(self, search_array=None, filter_array=None,size=200,
               to_return='*'):
        """
        searchArray is of the format : [
                                        ["toSearchFor", "fields, *to, search^3, in*" ],
                                        ["toSearchFor2", ...],
                                        ...
                                ]
        filterArray is of the format : [
                                        ["toSearchFor", "fields, *to, search^3, in*" ],
                                        ["field_to_filter_on", min_value, max_value],
                                        ...
                                ]
        toReturn is an array of fields to be returned in the results
        verbose = True to set verbosity level
        """
        res = None
        if filter_array is None:
            filter_array = []
        if search_array is None:
            search_array = []

        query = make_query(search_array, filter_array, to_return)
        es_connection = self.get_es_connection()
        try:
            res = es_connection.search(index=self._PRE_PROCESS_HARD, size=500, body=query, request_timeout=300)
            res = [r['_source'] for r in res['hits']['hits']]
        except Exception as e:
            print "----Elastic search error-----" + str(e)

        return res

    def count(self, cities=None, mandatory_skills=None, minexp=-1, maxexp=400):
        """
        cities is a vector of city names.
        mandatory_skills is a vector of skills that we need for sure in the results.
        """
        if mandatory_skills is None:
            mandatory_skills = []
        if cities is None:
            cities = []
        total = None
        count = 0
        for city in cities:
            filter_array = [[city, "locality"], ["exp_years", minexp, maxexp]]
            for skill in mandatory_skills:
                filter_array.append([skill, "preproc_skills_fuzzy"])
            query = make_query(filter_array=filter_array, to_return="*")

            es_connection = self.get_es_connection()
            total = es_connection.count(index=self._PRE_PROCESS_HARD, body=query)
            count += total

        return total

    def get_user_search_ids(self, user_id):
        """gets search_ids from es for user id"""
        if is_empty(user_id):
            return "Empty user id"
        ret = None
        query = make_query(search_array=[[user_id, "user_id", "search_ids"]], count_query='no')
        es_connection = self.get_es_connection()
        try:
            ret = es_connection.search(index=self._USERS, doc_type="user", body=query)
        except Exception as e:
            print "----Elastic search error-----" + str(e)

        return ret['hits']['hits']

    def update_search_id(self, user_id, list_of_search_ids, document_id):
        """updates search_ids list for user id"""
        ret = None
        if is_empty(user_id) or is_empty(list_of_search_ids) or is_empty(document_id):
            return "Supply valid arguments"
        body = {
            "user_id": user_id,
            "search_ids": list_of_search_ids
        }
        es_connection = self.get_es_connection()
        try:
            ret = es_connection.index(index=self._USERS, doc_type="user", body=body, id=document_id)
        except Exception as e:
            print "----Elastic search error-----" + str(e)

        return ret

    def get_cached_search(self, user_id, search_id):
        """gets cached search with sid for user_id"""
        if is_empty(user_id) or is_empty(search_id):
            return "Pass valid arguments"
        ret = None
        query = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"user_id": user_id}},
                        {"match": {"search_id": search_id}}
                    ]
                }
            }
        }
        es_connection = self.get_es_connection()
        try:
            ret = es_connection.search(index=self._SEARCHES, doc_type='search', body=query)

        except Exception as e:
            print "----Elastic search error-----" + str(e)

        return ret

    def fetch_search_document(self, search_id, user_id):
        if is_empty(user_id) or is_empty(search_id):
            return "Provide valid arguments"
        ret = None
        query = {
            "query": {
                "bool": {
                    "must": [
                        {"term": {"user_id": user_id}},
                        {"term": {"search_id": search_id}}
                    ]
                }
            }
        }
        es_connection = self.get_es_connection()
        try:
            ret = es_connection.search(index=self._SEARCHES, size=1, doc_type='search', body=query)
        except Exception as e:
            print "----Elastic search error-----" + str(e)
        return ret['hits']['hits']

    def cache_searches(self, search_id, search_cache, user_id, query, edit_flag):
        """saves the search with search id ,cache and user_id"""
        if is_empty(search_id) or is_empty(search_cache) or is_empty(user_id) or is_empty(edit_flag):
            return "Provide valid arguments"
        es_connection = self.get_es_connection()
        try:
            cache_ = {"search_id": search_id, "user_id": user_id, "query": query, "cache": search_cache}
            if str(edit_flag) == str(0):
                ret = es_connection.index(index=self._SEARCHES, doc_type='search', id=str(uuid.uuid4()), body=cache_)
            else:
                document = self.fetch_search_document(search_id, user_id)
                document_id = document[0]['_id']
                es_connection.delete(index=self._SEARCHES, doc_type="search", id=document_id)
                ret = es_connection.index(index=self._SEARCHES, doc_type="search", body=cache_, id=document_id)

        except Exception as e:
            print "----Elastic search error-----" + str(e)
            raise

        return ret

    def fetch_query_details(self, user_id):
        if is_empty(user_id):
            return "Provide valid arguments"
        ret = None
        body = {
            "_source": ["query"],
            "query": {
                "bool": {
                    "must": [
                        {"match": {"user_id": user_id}}
                    ]
                }
            }
        }
        es_connection = self.get_es_connection()
        try:
            ret = es_connection.search(index=self._SEARCHES, doc_type='search', body=body, size=MAX_SIZE)
        except Exception as e:
            print "------Elastic search error-----" + str(e)
        return ret['hits']['hits']

    def bulk_query(self, field, search_items_list, es_index=None, source="*"):
        if is_empty(field) or is_empty(search_items_list) or is_empty(es_index):
            return "Provide valid arguments"

        query = {
            "_source": source,
            'query': {
                'bool': {
                    'should': [

                    ]
                }
            }
        }

        template = {
            'constant_score': {
                'query': {
                    'term': {

                    }
                }
            }
        }

        for item in search_items_list:
            obj = deepcopy(template)
            obj['constant_score']['query']['term'][field] = item
            query['query']['bool']['should'].append(deepcopy(obj))

        ordered_list = []
        try:
            item_index = {}
            for index, item in enumerate(search_items_list):
                item_index[item] = index

            es_connection = self.get_es_connection()
            res = es_connection.search(index=es_index, body=query, size=SIZE, request_timeout=REQUEST_TIMEOUT)
            candidates = [i['_source'] for i in res['hits']['hits']]
            ordered_list = [0] * len(item_index)
            for each in candidates:
                real_index = item_index[each['unique_id']]
                ordered_list[real_index] = each
        except Exception as e:
            print (str(e))

        return ordered_list

    def fetch_search_details(self, search_id, user_id):
        if is_empty(search_id) or is_empty(user_id):
            return "Provide valid arguments"
        ret = None
        body = {
            "_source": ["query"],
            "query": {
                "bool": {
                    "must": [
                        {"term": {"user_id": user_id}},
                        {"term": {"search_id": search_id}}
                    ]
                }
            }
        }
        try:
            es_connection = self.get_es_connection()
            ret = es_connection.search(index=self._SEARCHES, doc_type='search', body=body, size=MAX_SIZE)
        except Exception as e:
            print "------Elastic search error-----" + str(e)
        return ret['hits']['hits']

    def update_equilateral(self, unique_id, databin_urls, databin_data, timestamp):
        if is_empty(unique_id) or is_empty(timestamp):
            return "Provide valid arguments"
        ret = None
        query = {
            'equilateral_data': databin_data,
            'other_urls': databin_urls,
            'timestamp': timestamp,
            'unique_id': unique_id
        }
        es_connection = self.get_es_connection()
        try:
            ret = es_connection.index(index=self._EQUILATERAL, doc_type='data', body=query)
        except Exception as e:
            print str(e)
        return ret

    def update_mercurial(self, unique_id, prediction, timestamp):
        if is_empty(unique_id) or is_empty(timestamp):
            return "Provide valid arguments"
        ret = None
        query = {
            'spa': prediction,
            'timestamp': timestamp,
            'unique_id': unique_id,
        }
        es_connection = self.get_es_connection()
        try:
            ret = es_connection.index(index=self._MERCURIAL, doc_type='data', body=query)
        except Exception as e:
            print str(e)

        return ret
