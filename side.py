import json, falcon, http.client, urllib.request, urllib.parse, urllib.error, base64
from key import TOKEN, MKEY

class status(object):
    def on_get(self, req, resp):
        resp.body = "{ \"status\": \"ok\"}"
        resp.status = falcon.HTTP_200

class find(object):
    def on_get(self, req, resp):
        token = req.get_header("token")
        if(token != TOKEN):
            resp.body = "{ \"error\": \"bad token\"}"
            resp.status = falcon.HTTP_403
            return
        faceId = req.get_header("faceId")
        faceList = req.get_header("faceList")

        headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': MKEY
        }
        params = urllib.parse.urlencode({
        })
        body = json.dumps({
            "faceId": faceId,
            "faceListId": faceList,
            "maxNumOfCandidatesReturned": 10,
            "mode": "matchFace"
        })
        try:
            conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/findsimilars?%s" % params, body, headers)
            response = conn.getresponse()
            data = json.load(response)
            resp.body = json.dumps(data)
            resp.status = falcon.HTTP_200
            conn.close()
        except Exception as e:
            print(e)
       
class detect(object):
    def on_get(self, req, resp):
        token = req.get_header("token")
        if(token != TOKEN):
            resp.body = "{ \"error\": \"bad token\"}"
            resp.status = falcon.HTTP_403
            return
        url = req.get_header("url")
        headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': MKEY
        }
        params = urllib.parse.urlencode({
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'recognitionModel': 'recognition_02',
            'returnRecognitionModel': 'false',
            'detectionModel': 'detection_02'
        })
        body = json.dumps({
            "url" : url
        })
        try:
            conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
            response = conn.getresponse()
            data = json.load(response)
            resp.status = falcon.HTTP_401
            resp.body = "{ \"error\": \"bad\"}"
            resp.body = "{ \"faceId\": \"" + data[0]["faceId"] + "\" }"
            resp.status = falcon.HTTP_200
            conn.close()
        except Exception as e:
            print(e)
       

