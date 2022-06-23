import papermill as pm
def lambda_handler(event, context):   
    pm.execute_notebook(
   's3://papermillbucket/notebook.ipynb',
   's3://papermillbucket/output.ipynb',
)
    response = {'text':'worked'}
    print(response['text'])
    return response['text']