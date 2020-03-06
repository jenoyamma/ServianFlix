import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource("dynamodb")

def split_to_chunks(lst, n):
    newLst = []
    for i in range(0, len(lst), n):
        newLst.append(lst[i:i + n])
    return(newLst)

def lambda_handler(event, context):
    req_type = event["req_type"]
    attribute = event["attribute"]

    movie_md = dynamodb.Table("movie_md")
    
    if req_type == 'genre':
        response = movie_md.query(
            IndexName='genre-index'
            , KeyConditionExpression=Key('genre').eq(attribute)
        )
        if len(response["Items"]) == 9:
            response = response
        elif len(response["Items"]) > 45:
            response = response["Items"][:44]
            response = split_to_chunks(response["Items"], 9)
        else:
            response = split_to_chunks(response["Items"], 9)
            
    elif req_type == 'single':
        response = movie_md.query(
            KeyConditionExpression=Key("movieId").eq(attribute)
        )
    
    return {
        'statusCode': 200,
        'body': response
    }
