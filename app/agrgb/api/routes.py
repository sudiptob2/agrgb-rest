from flask import Blueprint, Flask, request, Response
import jsonpickle
import numpy as np
import cv2
from flask_cors import CORS, cross_origin

from app.agrgb.ml.detector import Detect

mod = Blueprint('api', __name__)
CORS(mod)
detect = Detect()


# create the route
@mod.route('/detect', methods=['POST'])
def do_post():
    r = request
    imagestr = None
    imagestr = request.files["image"].read()  # here key of the file is 'image'

    # convert string of image data to uint8 numpy array
    npimg = np.fromstring(imagestr, np.uint8)
    # decode image
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    # do some fancy processing here....

    res = detect.predict(img)

    # build a response dict to send back to client
    response = {'disease': res}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")
