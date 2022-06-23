import papermill as pm
def lambda_handler(event, context):   
    pm.execute_notebook(
   'notebook.ipynb',
   'notebook_output.ipynb',
)
    response = {'text':'lamda is working'}
    print(response['text'])
    return response['text']