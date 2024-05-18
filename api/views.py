from django.http import JsonResponse
from big_query import query


def traer_actores(request):
    sql_query = "SELECT * FROM `sigeti-admin-364713.Gestion_Documental.Actores`"
    results = query(sql_query)
    data = [dict(row) for row in results]
    return JsonResponse(data, safe=False)
