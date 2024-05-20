from queries.big_query.query import query_normal as bigquery


def traer_sexo_edad_territorial(request, pk):
    sql = (
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
    return bigquery(sql)


def traer_infraeastructura_comunal(request, pk):
    sql = (
        "SELECT INFR_TOTMALOCAS, INFR_MALESCOLAR, INFR_SALUDTOT\
                 FROM `sigeti-admin-364713.censo_632.BD_comunidades`\
                 WHERE ID = "
        + str(pk)
        + ";"
    )
    return bigquery(sql)
