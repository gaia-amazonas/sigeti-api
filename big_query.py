from google.cloud import bigquery
import os

# Ensure the Google Application Credentials environment variable is set
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS"
)

client = bigquery.Client()


def query(sql_query):
    query_job = client.query(sql_query)
    results = query_job.result()
    return results
