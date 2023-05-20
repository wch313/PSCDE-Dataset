import keras.backend as K
import tensorflow as tf
from keras.layers import  Activation, Add, Layer

class BSRAh(Layer):
    def __init__(self,
                 gamma_initializer=tf.zeros_initializer(),
                 gamma_regularizer=None,
                 gamma_constraint=None,
                 **kwargs):

        self.gamma_initializer = gamma_initializer
        self.gamma_regularizer = gamma_regularizer
        self.gamma_constraint = gamma_constraint
        self.Add = Add()
        self.softmax = Activation('softmax')

        super(BSRAh, self).__init__(**kwargs)

    def build(self, input_shape):
        self.gamma = self.add_weight(shape=(1, ),
                                     initializer=self.gamma_initializer,
                                     name='gamma',
                                     regularizer=self.gamma_regularizer,
                                     constraint=self.gamma_constraint)
        self.built = True

    def compute_output_shape(self, input_shape):
        return input_shape

    def call(self, input):

        [batch, h, w, filters] = input.shape.as_list()
        inputh     = tf.transpose(input, (0,3,2,1))
        Q  = tf.reduce_mean(inputh,axis=3,keepdims=True)
        QQ = tf.reduce_max(inputh,axis=3,keepdims=True)
        Q_SUM = self.Add([Q,QQ])
        Q1 = K.reshape(Q_SUM, (-1, w , filters))
        Q2 = tf.transpose(Q1, (0, 2, 1))
        aTa = K.batch_dot(Q2, Q1)
        softmax_aTa = self.softmax(aTa)
        vec_a = K.reshape(input, (-1, h*w , filters))
        aaTa = K.batch_dot(vec_a, softmax_aTa)
        aaTa = K.reshape(aaTa, (-1, h, w, filters))

        out = self.gamma*aaTa+input

        return out
    def get_config(self):
      config = super().get_config().copy()

      config.update({"gamma_initializer":self.gamma_initializer,"gamma_regularizer":self.gamma_regularizer,
               "gamma_constraint":self.gamma_constraint})

      return config

class BSRAw(Layer):
    def __init__(self,
                 gamma_initializer=tf.zeros_initializer(),
                 gamma_regularizer=None,
                 gamma_constraint=None,
                 **kwargs):

        self.gamma_initializer = gamma_initializer
        self.gamma_regularizer = gamma_regularizer
        self.gamma_constraint = gamma_constraint
        self.Add = Add()
        self.softmax = Activation('softmax')

        super(BSRAw, self).__init__(**kwargs)

    def build(self, input_shape):
        self.gamma = self.add_weight(shape=(1, ),
                                     initializer=self.gamma_initializer,
                                     name='gamma',
                                     regularizer=self.gamma_regularizer,
                                     constraint=self.gamma_constraint)

        self.built = True

    def compute_output_shape(self, input_shape):
        return input_shape


    def call(self, input):

        [batch, h, w, filters] = input.shape.as_list()

        vec_a = K.reshape(input, (-1, h*w , filters))
        inputw     = tf.transpose(input, (0,1,3,2))
        q   = tf.reduce_mean(inputw,axis=3,keepdims=True)
        qq1 = tf.reduce_max(inputw,axis=3,keepdims=True)
        q_SUM =self.Add([q,qq1])
        q1 = K.reshape(q_SUM, (-1, h, filters))
        q2 = tf.transpose(q1, (0, 2, 1))
        ATa = K.batch_dot(q2, q1)
        Softmax_aTa = self.softmax(ATa)
        AATa = K.batch_dot(vec_a, Softmax_aTa)
        AATa = K.reshape(AATa, (-1, h, w, filters))
        out =  input+self.gamma*AATa

        return out
    def get_config(self):
      config = super().get_config().copy()

      config.update({"gamma_initializer":self.gamma_initializer,"gamma_regularizer":self.gamma_regularizer,
               "gamma_constraint":self.gamma_constraint})

      return config


# 创建一个随机输入张量，形状为(batch_size, height, width, channels)
batch_size = 32
height = 128
width = 64
channels = 3
input_tensor = tf.random.normal((batch_size, height, width, channels))

# 创建 BSRA 层的实例
bsrah_layerh = BSRAh()
bsrah_layerw = BSRAw()

# 将输入张量传递给 BSRA 层的 call 方法
output_tensorh = bsrah_layerh(input_tensor)
output_tensorw = bsrah_layerw(input_tensor)

# 打印输出张量的形状
print(output_tensorh.shape)

print(output_tensorw.shape)