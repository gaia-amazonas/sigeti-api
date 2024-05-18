from django.http import JsonResponse
from big_query import query


def traer_sexo_edad_territorial(request, pk):
    sql_query = (
        "SELECT sexo, edad\
                FROM `sigeti-admin-364713.censo_632.BD_personas`\
                WHERE territorio = (SELECT territorio\
                FROM (\
                    SELECT DISTINCT territorio\
                    FROM `sigeti-admin-364713.censo_632.BD_familias`\
                    ORDER BY territorio\
                    LIMIT "
        + str(pk)
        + ") AS subquery\
                ORDER BY territorio DESC\
                LIMIT 1);"
    )
    results = query(sql_query)
    data = [dict(row) for row in results]
    return JsonResponse(data, safe=False)
