# -*- coding: utf-8 -*-
'''
svakulenko
9 Nov 2017
'''
from elasticsearch import Elasticsearch
from all_settings import INDEX


mapping = {
      'settings': {
        # just one shard, no replicas for testing
        'number_of_shards': 1,
        'number_of_replicas': 0,
      },
      'mappings': {
        'tweets': {
          'properties': {
            'tweet': {'type': 'text', 'analyzer': 'german'},
            # 'tweet': {'type': 'text', 'analyzer': 'standard'},
          }
        }
      }
    }

def create_index(index_name):
    es = Elasticsearch()
    # reset index
    try:
        # es.indices.delete(index=index_name)
        es.indices.create(index=index_name, body=mapping)
    except Exception as e:
        print (e)

if __name__ == '__main__':
    create_index(INDEX)
