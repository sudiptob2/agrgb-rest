from flask import Blueprint,Flask, request, Response
import jsonpickle
import numpy as np
import cv2

#define the module
mod = Blueprint('api', __name__)

#create the route
@mod.route('/detect', methods=['POST'])
def detect():
    r = request
    imagestr = None
    imagestr = request.files["image"].read() # here key of the file is 'image'

    # convert string of image data to uint8 numpy array
    npimg = np.fromstring(imagestr, np.uint8)
    # decode image
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")
    #return {'message': 'got the image'}
