# flask_convert_json_to_h5

### What it does
This creates a server that converts the received tfjs model files, which are in format of .json and .bin, into more commnon tensor flow model file, .h5 file.  
For detailed explanaion on how to send .json and .bin files, and fetch back the .h5 file, check out the tfjs api documents.

### To build
```
docker build -t osy044/json_to_h5_converter:0.0.2 .
```

### To run
```
docker container run -d -p 5050:5050 osy044/json_to_h5_converter:0.0.2
```




### Compatibility issue
This converted h5 file may include the mobilenetv2 provided by google. However, this converted h5 may require some dependency. Otherwise the error will occur when model is loaded. Below shows the dependency with tensorflow and keras packages.



For below four versions, the following code needs to be added for the custom activation. Otherwise the following error will occur.
+ tensorflow==2.3
+ tensorflow==2.4
+ tensorflow==2.5
+ tensorflow==2.6

The error might look like this
```
ValueError: Unknown activation function: relu6
```

To resolve this issue, following code snippet has to be added to your python code
```
from tensorflow.keras import layers
from tensorflow.keras.utils import get_custom_objects
from tensorflow.python.keras import backend as K

def relu6(x):
  return K.relu(x, max_value=6)
get_custom_objects().update({'relu6': relu6})
```
  
  
For the other versions, some other error may occur.
+ tensorflow==2.7
+ tensorflow==2.8

```
ImportError: cannot import name 'dtensor'
```

For this error, keras packages has to be downgraded to 2.6.  
If the keras version is already 2.6, try upgrading it first to 2.10, and then downgrade it again back to 2.6 or 2.8