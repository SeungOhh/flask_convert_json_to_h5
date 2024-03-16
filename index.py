import os
import json
import tempfile

from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin

import tensorflow as tf
from tensorflow.keras.utils import get_custom_objects
from tensorflow.python.keras import backend as K
import tensorflowjs as tfjs


#%% custom layer for mobilenetv2
def relu6(x):
  return K.relu(x, max_value=6)
get_custom_objects().update({'relu6': relu6})


#%%
app = Flask(__name__)
CORS(app)

@app.route('/running', methods=['GET'])
@cross_origin()
def running():
    return "Server is running"

@app.route('/upload', methods=['POST'])
@cross_origin()
def upload():
    print("\n\n\n")
    print(request.files)
    print("\n\n\n")

    temp_dir = tempfile.mkdtemp()
    json_dir = os.path.join(temp_dir, 'model.json')
    bin_dir = os.path.join(temp_dir, 'model.weights.bin')
    model_dir = os.path.join(temp_dir, "keras_model.h5")
    print(temp_dir)

    # json save
    file_json = request.files['model.json']
    file_json = json.load(file_json) # load stringified json
    with open(json_dir, 'w') as f:
        f.write(file_json + '\n')
    print('----------json-----------')

    # bin save
    file_bin = request.files['model.weights.bin']
    file_bin.save(bin_dir)
    print('----------bin-----------')

    # h5 convert
    model = tfjs.converters.load_keras_model(json_dir)
    model.summary()
    model.save(model_dir)


    return send_file(model_dir, as_attachment=True, download_name='keras_model.h5', mimetype='application/octet-stream')
    # return Response(200)

if __name__ == '__main__':
    # Run the application on all network interfaces and port 5050
    app.run(debug=True, host="0.0.0.0", port=5050)