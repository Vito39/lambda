import json
import boto3


def respond(res):
    return {
        'statusCode': '200',
        'body': json.dumps(res['body'], indent=2)
    }

def lambda_handler(event, context):
    #return respond(event)
    body = json.loads(event['body'])
    fname = body.get("firstname")
    lname = body.get("lastname")
    
    if fname==None or lname==None:
        return {
            'statusCode': '200',
            'body':"Hello world I don't know your name",
            'headers' : {
            'content-Type' : 'application/json'
            }
        }
    else:
        return {
            'statusCode': '200',
            'body':'Hello '+ fname + ' ' + lname,
            'headers' : {
            'content-Type' : 'application/json'
            }
        }    
    raise Exception('Something went wrong')

