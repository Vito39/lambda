import boto3
from boto3.dynamodb.conditions import Key
import json


def handler(event, context):

   client = boto3.resource('dynamodb')
   table = client.Table('second_table')
   body = json.loads(event['body'])
   name = body.get("name")
   if name==None or name=="":
      return {
         'statusCode': '200',
         'body' : 'Please Enter the Name'
      }
    
   Has_name = table.query(
      KeyConditionExpression=Key('name').eq(name)
   )   
   Items=Has_name['Items']
   
   if  len(Items)>0: 
       return {
         'statusCode': '200',
         'body' : json.dumps(Has_name['Items'])
      }
   else :
        return {
         'statusCode': '200',
         'body' : 'Not exist'
      } 
      
