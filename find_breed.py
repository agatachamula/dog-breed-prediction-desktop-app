import tensorflow as tf
import sys
import os
import csv
from tkinter import Tk, Label, Button, StringVar, filedialog, Frame, simpledialog




def predict(image_path):

    #load image from file
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    # load model
    with tf.gfile.FastGFile("trained_model/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, \
                                   {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    #return 3 top predictions
    return top_k[0:3]


def decode_breed(breed_id):
    # read labels into file
    label_lines = [line.rstrip() for line in tf.gfile.GFile("trained_model/retrained_labels.txt")]
    breed=label_lines[breed_id]

    return breed

