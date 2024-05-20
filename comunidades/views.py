from queries.big_query.query import query_normal as bigquery


def traer_nombres(request):
    sql = "SELECT ID, ID_FORM\
        FROM `sigeti-admin-364713.censo_632.BD_comunidades`;"
    return bigquery(sql)
