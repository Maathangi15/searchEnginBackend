from elasticsearch import Elasticsearch

def standard_search(query, page, rows_per_page):
    if(query is None or query == ''):
        details = {
            "query": {
                'bool': {
                    "must": {
                        "match_all": {}
                    }
                },
            },
            "size": rows_per_page,
            "from": (page)*rows_per_page
        }
    else:
        details = {
            "query": {
                "query_string": {
                    "query":    query
                }
            },
            "size": rows_per_page,
            "from": (page)*rows_per_page
        }
    return details
    

INDEX = 'hit_tamil_songs'
client = Elasticsearch(HOST="http://localhost", PORT=9200,)#i disabled auth so no need auth details


def search(query,  page, rows_per_page):
    query_body = standard_search(query,  page, rows_per_page)
    print('Making Basic Search ')
    res = client.search(index=INDEX, details=query_body)
    return res
