from posixpath import join
from django.shortcuts import render

# Create your views here.
import os, io
from draw_vertice import drawVertices
from google.cloud import vision 
import pandas as pd 

os.environ['THUMSTACK_APPLICATION_CREDENTIALS'] = r'serviceAccountToken.json'
client_path  = vision.ImageannotatorClient()

file_name = 'logothumbstack'
image_folder = './images/'
image_path = os.path,join(image_folder, file_name)

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.logo_detection(image=image)
    logos = response.logo_annotations

    for logo in logos:
        print('logo description:', logo description)
        print('confidence score:',logo.score)
        print('-'*50)
        Vertices = logo.bounding_poly.vertices
        print('vertices values{0}'.format(vertices))
        drawVertices(content, vertices,logo.description)
