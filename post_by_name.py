import boto3
from boto3.dynamodb.conditions import Key
import json


def handler(event, context):

   client = boto3.resource('dynamodb')

   table = client.Table('second_table')
   
   body = json.loads(event['body'])
   
   name = body.get("name")

   if name==None or name=="" :
      return {
         'statusCode': '200',
         'body' : 'Please Enter the Name'
      }
      
   Has_name = table.get_item(
      Key={'name':name}
   )   
   
   
 
   
   if  'Item' in Has_name: 
       return {
         'statusCode': '200',
         'body' : name + 'Already added'
      }
      
      
      
   response = table.put_item(

       Item=body

   )

   return {

       'statusCode': response['ResponseMetadata']['HTTPStatusCode'],

       'body': 'Record ' + name + ' added'

   }
