from pathlib import Path
import os

def deleteFile(path):
    if path != '/images/model.png':
        BASE_DIR = Path(__file__).resolve().parent.parent
        final_path = str(BASE_DIR) +'/static/images/user_images/' + str(path)
        if os.path.exists(final_path):
            os.remove(final_path)
        return True
    else:
        return False

def sumOfData(data):
    sum = 0
    for x in data:
        sum += float(x['value'])
    
    sum = round(sum, 2)
    sum = "{:,}".format(sum)
    try:
        index = str(sum).index('.')
    except:
        index = -1

    if index == -1:
        return sum + ".00"
    else:
        if(index == len(sum)-2):
            return sum + "0"
        elif(index == len(sum)-3):
            return sum

def createPercentage(data):
    dict = {}

    for element in data:
        if element['category'] in dict:
            dict[element['category']] += float(element['value'])
        else:
            dict[element['category']] = float(element['value'])

    for element in dict:
        dict[element] = round(dict[element],2)
        
    return dict
        
    
