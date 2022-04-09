import json
import shutil

with open('C:/Users/pklimczak/Desktop/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_val.json') as json_file:
    json_data = json.load(json_file)
    
i = 0

for item in json_data:
    i = i + 1
    item_path = 'C:/Users/pklimczak/Desktop/bdd100k_images_100k/bdd100k/images/100k/val/' + item['name']
    print("Iterate no.:" + str(i))
    print(item['name'])
    if item['attributes']['timeofday'] == 'daytime':
        shutil.copy(item_path, 'C:/Users/pklimczak/Desktop/bdd100k_images_100k/bdd100k/images/testB/' + item['name'])

    elif item['attributes']['timeofday'] == 'night':
        shutil.copy(item_path, 'C:/Users/pklimczak/Desktop/bdd100k_images_100k/bdd100k/images/testA/' + item['name'])

    else :
        shutil.copy(item_path, 'C:/Users/pklimczak/Desktop/bdd100k_images_100k/bdd100k/images/testElse/' + item['name'])