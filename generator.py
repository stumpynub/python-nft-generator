import os
import random 
import json
import util
from PIL import Image

NAME : str = 'your nft'
SIZE : tuple = (1000, 1000)
LAYERS_ROOT_DIR : str = 'layers'
OUTPUT_DIR : str = 'output'
ITERATIONS : int = 10
FORMAT : str = 'png'
CLEAR_OUTPUT : bool = True

current_iteration : int = 1
layers_dirs : list = []
seeds : list = []


# get all subdirectories of LAYERS_ROOT_DIR
for dir in os.walk(LAYERS_ROOT_DIR, True): 
    if dir[0] != LAYERS_ROOT_DIR: 
        layers_dirs.append(dir[0])

# remove output files when ran
for file in os.listdir(OUTPUT_DIR): 
    if CLEAR_OUTPUT: 
        os.remove(os.path.join(OUTPUT_DIR, file))


def generate_image(name:str):
    ''' Generate image based on given layers

        parameters: 
            name (str): Name of the saved image and metadata

    '''
    global current_iteration
    base_img = Image.new(mode="RGBA", size=SIZE)
    
    seed = []
    
    # layer the image based of the directory order 
    for path in layers_dirs:        
        rand = random.randrange(0, len(os.listdir(path)))
        seed.append(rand)
        img = Image.open(os.path.join(path, os.listdir(path)[rand])).convert('RGBA')
        base_img.paste(img, mask=img)
    
    # If a seed is not found in seeds[], add new seed and create image 
    if seed not in seeds: 
        seeds.append(seed)
        current_iteration += 1
        base_img.save(os.path.join(OUTPUT_DIR, name + f".{FORMAT}"))
        data = open(os.path.join(OUTPUT_DIR, f'{name}.json'), 'w')
        json.dump(util.create_metadata(name, "Your NFT Description", current_iteration, "Your NFT URL"), data)

    else: 
        print('Seed found')

while current_iteration <= ITERATIONS: 
    generate_image(f'{NAME}#{current_iteration}')

