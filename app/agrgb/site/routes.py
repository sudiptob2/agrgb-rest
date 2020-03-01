from flask import Blueprint
import requests
import json
import cv2


mod = Blueprint('site', __name__)

@mod.route('/test')
def test():
    addr = 'http://localhost:5000' #default domain of the server
    test_url = addr + '/api/detect'# address of the api to the api where request to be sent

    # prepare headers for http request
    content_type = 'image/jpeg'
    headers = {'content-type': content_type}

    img = cv2.imread('static/lena.jpg')
    # encode image as jpeg
    _, img_encoded = cv2.imencode('.jpg', img)
    # send http request with image and receive response
    response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
    # decode response
    # print(json.loads(response.text))
    return json.loads(response.text)

    # expected output: {u'message': u'image received. size=124x124'}
