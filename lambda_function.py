import papermill as pm
def lambda_handler(event, context):   
    response = {'text':'lamda is working'}
    print(response['text'])
    return response['text']