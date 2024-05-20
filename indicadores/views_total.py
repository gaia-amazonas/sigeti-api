from queries.big_query.query import query_normal as bigquery


def traer_porcentaje_total(request, variable):
    sql = (
        "SELECT\
            SUM(Castellano) AS Castellano_Frequency,\
            SUM(Portugues) AS Portugues_Frequency,\
            SUM(Bora) AS Bora_Frequency,\
            SUM(Inaa) AS Inaa_Frequency,\
            SUM(Inga) AS Inga_Frequency,\
            SUM(Vina) AS Vina_Frequency,\
            SUM(Bara) AS Bara_Frequency,\
            SUM(Cubeo) AS Cubeo_Frequency,\
            SUM(Itano) AS Itano_Frequency,\
            SUM(Muina) AS Muina_Frequency,\
            SUM(Muruy) AS Muruy_Frequency,\
            SUM(Yagua) AS Yagua_Frequency,\
            SUM(Yauna) AS Yauna_Frequency,\
            SUM(Yeral) AS Yeral_Frequency,\
            SUM(Yujup) AS Yujup_Frequency,\
            SUM(Baniwa) AS Baniwa_Frequency,\
            SUM(Cocama) AS Cocama_Frequency,\
            SUM(Desano) AS Desano_Frequency,\
            SUM(Eduria) AS Eduria_Frequency,\
            SUM(Ingano) AS Ingano_Frequency,\
            SUM(M_N_Ka) AS M_N_Ka_Frequency,\
            SUM(Macuje) AS Macuje_Frequency,\
            SUM(Macuna) AS Macuna_Frequency,\
            SUM(Matapi) AS Matapi_Frequency,\
            SUM(Okaina) AS Okaina_Frequency,\
            SUM(Piaroa) AS Piaroa_Frequency,\
            SUM(Tatuyo) AS Tatuyo_Frequency,\
            SUM(Ticuna) AS Ticuna_Frequency,\
            SUM(Tucano) AS Tucano_Frequency,\
            SUM(Tuyuca) AS Tuyuca_Frequency,\
            SUM(Yucuna) AS Yucuna_Frequency,\
            SUM(Yuruti) AS Yuruti_Frequency,\
            SUM(Ciriano) AS Ciriano_Frequency,\
            SUM(Guanano) AS Guanano_Frequency,\
            SUM(Huitoto) AS Huitoto_Frequency,\
            SUM(Letuama) AS Letuama_Frequency,\
            SUM(Majinna) AS Majinna_Frequency,\
            SUM(Miranna) AS Miranna_Frequency,\
            SUM(Piapoco) AS Piapoco_Frequency,\
            SUM(Pn_M_Na) AS Pn_M_Na_Frequency,\
            SUM(Puinave) AS Puinave_Frequency,\
            SUM(Quechua) AS Quechua_Frequency,\
            SUM(Sikuani) AS Sikuani_Frequency,\
            SUM(Taiwano) AS Taiwano_Frequency,\
            SUM(Tatuano) AS Tatuano_Frequency,\
            SUM(Tujupda) AS Tujupda_Frequency,\
            SUM(Barasano) AS Barasano_Frequency,\
            SUM(Carapana) AS Carapana_Frequency,\
            SUM(Carijona) AS Carijona_Frequency,\
            SUM(Kawiyari) AS Kawiyari_Frequency,\
            SUM(Pisamira) AS Pisamira_Frequency,\
            SUM(Tanimuca) AS Tanimuca_Frequency,\
            SUM(NNengatu) AS NNengatu_Frequency,\
            SUM(Curripaco) AS Curripaco_Frequency,\
            SUM(Guayabero) AS Guayabero_Frequency,\
            SUM(Piratapuyo) AS Piratapuyo_Frequency\
            FROM `sigeti-admin-364713.censo_632."
        + variable
        + "`;"
    )

    return bigquery(sql)
