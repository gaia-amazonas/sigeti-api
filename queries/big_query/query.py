from django.http import JsonResponse
from big_query import query


def query_normal(sql):
    results = query(sql)
    data = [dict(row) for row in results]
    return JsonResponse(data, safe=False)
