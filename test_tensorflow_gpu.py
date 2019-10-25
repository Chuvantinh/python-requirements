import tensorflow as tf
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))


import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
