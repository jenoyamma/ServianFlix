from json import dumps
from scipy.sparse import lil_matrix
from sagemaker import Session
from sagemaker.predictor import RealTimePredictor, json_deserializer

sm_sess = Session()

def build_spare_matrix_payload(movie_id):
    # 943 - nb_users_train
    x_movie_id = 943 + int(movie_id)

    # 2625 - nb_features
    X_new = lil_matrix((1, 2625)).astype('float32')
    X_new[0, 944] = 1
    X_new[0, x_movie_id] = 1

    payload = X_new[0].toarray()

    return(payload)

def post_process(result):
    score = result["predictions"][0]["score"]
    pp_score = round(score * 100, 2)
    predicted_label = result["predictions"][0]["predicted_label"]
    
    if predicted_label==1:
        txt = "Chance that you will like this: " + str(pp_score)
    else:
        txt = "Chance that you will like this: " + str(round(100 - pp_score, 2))
        
    return(txt)

def fm_serializer(data):
    js = {'instances': []}
    for row in data:
        js['instances'].append({'features': row.tolist()})
    return dumps(js)

def lambda_handler(event, context):
    sm_fm_endpoint = event["sm_fm_endpoint"]
    attribute = event["attribute"]

    fm_predictor = RealTimePredictor(endpoint = sm_fm_endpoint, sagemaker_session = sm_sess)
    
    fm_predictor.content_type = 'application/json'
    fm_predictor.serializer = fm_serializer
    fm_predictor.deserializer = json_deserializer

    payload = build_spare_matrix_payload(attribute)

    result = fm_predictor.predict(payload)

    pp_result = post_process(result)
    
    return {
        'statusCode': 200,
        'body': pp_result
    }
