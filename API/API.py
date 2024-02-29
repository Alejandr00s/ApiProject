from sodapy import Socrata
import pandas as pd
from tabulate import tabulate


def get_database(department_name, requests_limit):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr", departamento_nom=department_name, limit=requests_limit)
    results_df = pd.DataFrame.from_records(results)
    headers = ['ciudad_municipio_nom', 'departamento_nom', 'edad', 'fuente_tipo_contagio', 'estado']
    print(tabulate(results_df[headers], headers=["Ciudad de ubicación",
                                                 "Departamento", "Edad", "Tipo","Estado" ], tablefmt='pretty'))
