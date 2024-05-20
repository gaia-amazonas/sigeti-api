from queries.big_query.query import query_normal as bigquery


def traer_nombres(request):
    sql = "WITH RankedTerritorios\
        AS (SELECT ID, territorio, ROW_NUMBER()\
            OVER (PARTITION BY territorio ORDER BY ID) as rn\
                FROM `sigeti-admin-364713.censo_632.BD_familias`)\
                    SELECT ID, territorio\
                        FROM RankedTerritorios\
                            WHERE rn = 1\
                                ORDER BY territorio;"
    return bigquery(sql)
