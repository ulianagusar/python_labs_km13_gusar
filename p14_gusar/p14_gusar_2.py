import json

with open('image_info_test-dev2017.json') as file:#open file
    coco = json.load(file)
image_elem=len(coco["images"])#determining the number of elements
categories_elem=len(coco["categories"])
print("number of images :",image_elem)
print("number of categories :",categories_elem)
max=0
for photo in coco["images"] :
    if photo["file_name"]=="000000000001.jpg":
        print("photo url :",photo["coco_url"])
        print("photo height :",photo["height"])
        print("photo width :",photo["width"])
        print("photo id :",photo["id"])
    if int(photo["id"])>max :#determining the largest number
        max=photo["id"]
        name_max=photo["file_name"]
print("the name of the photo number of the largest number :",name_max)