# encoding=utf-8
import os
import time
import itertools
import sys
import numpy as np
import tensorflow as tf
import udc_model
import udc_hparams
import udc_metrics
import udc_inputs
from models.dual_encoder import dual_encoder_model
from models.helpers import load_vocab
import jieba

tf.flags.DEFINE_string("model_dir", None, "Directory to load model checkpoints from")
tf.flags.DEFINE_string("vocab_processor_file", "./data/vocab_processor.bin", "Saved vocabulary processor file")
tf.flags.DEFINE_string("vocab", "./data/vocabulary.txt", "Vocabulary file")
FLAGS = tf.flags.FLAGS

if not FLAGS.model_dir:
  print("You must specify a model directory")
  sys.exit(1)

def tokenizer_fn(iterator):
  return (x.split(" ") for x in iterator)

# Create vocabulary ourselves or load saved one
if not FLAGS.vocab_processor_file:
  vp = tf.contrib.learn.preprocessing.VocabularyProcessor(100000)
  vp.fit(open(FLAGS.vocab_processor_file))
  vp.save('./data/vocab_processor.bin')
else:
  vp = tf.contrib.learn.preprocessing.VocabularyProcessor.restore(
    FLAGS.vocab_processor_file)

# Load your own data here
INPUT_CONTEXT1 = jieba.cut("早上好,你明天准备干什么啊")
INPUT_CONTEXT=( " ".join(INPUT_CONTEXT1))


POTENTIAL_RESPONSES1= ["你好啊，早上吃饭了吗","我们明天去马尔代夫度蜜月吧飞机票订好了","明天晚上有百年校庆晚会，想去看吗"]
POTENTIAL_RESPONSES=[]

for d in POTENTIAL_RESPONSES1:
  seg_list = jieba.cut(d)
  temp=(" ".join(seg_list))
  POTENTIAL_RESPONSES.append(temp)





def get_features(context, utterance):
  context_matrix = np.array(list(vp.transform([context])))
  utterance_matrix = np.array(list(vp.transform([utterance])))
  context_len = len(context.split(" "))
  utterance_len = len(utterance.split(" "))
  features = {
    "context": tf.convert_to_tensor(context_matrix, dtype=tf.int64),
    "context_len": tf.constant(context_len, shape=[1,1], dtype=tf.int64),
    "utterance": tf.convert_to_tensor(utterance_matrix, dtype=tf.int64),
    "utterance_len": tf.constant(utterance_len, shape=[1,1], dtype=tf.int64),
  }
  return features, None

if __name__ == "__main__":
  hparams = udc_hparams.create_hparams()
  model_fn = udc_model.create_model_fn(hparams, model_impl=dual_encoder_model)
  estimator = tf.contrib.learn.Estimator(model_fn=model_fn, model_dir=FLAGS.model_dir)

  print("Context: {}".format(INPUT_CONTEXT))
  for r in POTENTIAL_RESPONSES:
    prob = estimator.predict(input_fn=lambda: get_features(INPUT_CONTEXT, r))
    for pred_dict in zip(prob):
      print("{}: {}".format(r, pred_dict[0]))