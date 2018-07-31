#encoding=utf-8

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
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
import json

tf.flags.DEFINE_string("model_dir", "./runs/1532678030/", "Directory to load model checkpoints from")
tf.flags.DEFINE_string("vocab_processor_file", "./data/vocab_processor.bin", "Saved vocabulary processor file")
tf.flags.DEFINE_string("vocab", "./data/vocabulary.txt", "Vocabulary file")
FLAGS = tf.flags.FLAGS

if not FLAGS.model_dir:
  print("You must specify a model directory")
  sys.exit(1)

def tokenizer_fn(iterator):
  return (x.split(' ') for x in iterator)

# Create vocabulary ourselves or load saved one
if not FLAGS.vocab_processor_file:
  vp = tf.contrib.learn.preprocessing.VocabularyProcessor(100000)
  vp.fit(open(FLAGS.vocab_processor_file))
  vp.save('./data/vocab_processor.bin')
else:
  vp = tf.contrib.learn.preprocessing.VocabularyProcessor.restore(
    FLAGS.vocab_processor_file)

# Load your own data here
INPUT_CONTEXT0 = " ".join(sys.argv[1:])
INPUT_CONTEXT1 = jieba.cut(INPUT_CONTEXT0)
INPUT_CONTEXT=( " ".join(INPUT_CONTEXT1))


POTENTIAL_RESPONSES1= ["控制指的是减少系统安全漏洞的保护性动作”,”保险性反映系统导致人员伤害/死亡，或造成对环境损害的可能性","嵌入式系统是用来控制或者监视机器、装置、工厂等大规模设备的系统","人工智能是研究、开发用于模拟、延伸和扩展人的智能的理论、方法、技术及应用系统的一门新的技术科学","系统失效指的是在某个时刻，系统发生未能够提供所期望服务的事件”,”系统错误指的是不符合系统规约的系统行为","威胁指的是潜在引起危害的系统状态”,”控制指的是减少系统安全漏洞的保护性动作","安全漏洞指的是可能被利用来产生危害的系统弱点”,”攻击指的是对系统安全漏洞的利用","安全性主要采用安全漏洞分析法。”,”安全隐患是指因安全问题所可能造成的系统危害","安全性是可用性、可靠性和保险性的前提条件。”,”安全性主要采用安全漏洞分析法","安全性是反映系统抵制意外或恶意侵入能力的整体性系统属性","系统缺陷是指不正确的系统状态。不符合系统设计者期望的系统状态","系统失效指的是在某个时刻，系统发生未能够提供所期望服务的事件”,”系统错误指的是不符合系统规约的系统行为","系统错误管理是实现高可用性系统的关键","人为错误是指人为引起的系统缺陷”,”杜绝系统失效的有效方法是防止与纠正系统错误，以及系统失效可以利用内建的保护机制来减少损失","系统缺陷是指不正确的系统状态,例如，不符合系统设计者期望的系统状态","系统错误管理是实现高可用性系统的关键”,”系统失效指的是在某个时刻，系统发生未能够提供所期望服务的事件”,”系统错误指的是不符合系统规约的系统行为","可靠性指的是在给定的时间内、给定的环境下、为给定目的而执行的系统操作保持无错的概率","系统可依赖性用以下四个维度来间接度量：可用性（Availability）、可靠性（Reliability）、保险性（Safety）和安全性(Security)","系统可依赖性应用在非常重要场合的系统，如航空电子、汽车电子等产品","系统可依赖性反映了用户对于系统按照其期望正常运行的信心程度","系统可依赖性等价于系统的可信度","系统可依赖性等价于系统的可信度。”,”系统可依赖性反映了用户对于系统按照其期望正常运行的信心程度","行动学习小组的目标是通过团队协作，学以致用，在完成课程项目的同时，高效实现个人的课程学习目标","行动学习是一种综合的学习模式，是学习知识、分享经验、创造性研究解决问题和实际行动四位一体的方法","行动学习的力量来源于小组成员对已有知识和经验的相互质疑和在行动基础上的深刻反思","行动学习法是由英国管理学思想家雷格·瑞文斯在1940年发明的","行动学习法是小型团队共同解决组织实际存在问题的过程和方法","行动学习不仅关注问题的解决，也关注团队成员的学习发展以及整个组织的进步","孔悝，卫庄公蒯聩的外甥。","早上好，今天天气不错，那你吃饭了吗？"]
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

  #print("Context: {}".format(INPUT_CONTEXT))
  for r in POTENTIAL_RESPONSES:
    prob = estimator.predict(input_fn=lambda: get_features(INPUT_CONTEXT, r))
    for pred_dict in zip(prob):
      print("{}: {}".format(r, pred_dict[0]))