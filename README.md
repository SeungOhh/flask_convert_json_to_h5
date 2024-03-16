# flask_convert_json_to_h5

###To build
docker build -t osy044/json_to_h5_converter:0.0.2 .

###To run
docker container run -d -p 5050:5050 osy044/json_to_h5_converter:0.0.2

###What it does
This converts the tfjs default model files, which are in format of .json and .bin, into .h5 file. 

###Compatibility issue
This converted h5 file may include the mobilenetv2 provided by google. However, this converted h5 may require some dependency. Otherwise the error will occur when model is loaded. Below shows the dependency with tensorflow and keras packages.

For below four versions, the following code needs to be added for the custom activation. Otherwise the following error will occur.
tensorflow==2.3
tensorflow==2.4
tensorflow==2.5

code 1
ValueError: Unknown activation function: relu6

code 1
from tensorflow.keras import layers
from tensorflow.keras.utils import get_custom_objects
from tensorflow.python.keras import backend as K

def relu6(x):
  return K.relu(x, max_value=6)
get_custom_objects().update({'relu6': relu6})
