from pathlib import Path
import os
import datetime

def deleteFile(path):
    if path != '/images/model.png':
        BASE_DIR = Path(__file__).resolve().parent.parent
        final_path = str(BASE_DIR) +'/static/images/user_images/' + str(path)
        if os.path.exists(final_path):
            os.remove(final_path)
        return True
    else:
        return False

def sumOfData(data, start, end):
    sum = 0
    for element in data:
        if (element['date_created']).date() >= start and (element['date_created']).date() <= end:
            sum += float(element['value'])
    
    sum = round(sum, 2)
    return sum

def createPercentage(data, start, end):
    dict = {}

    for element in data:
        if (element['date_created']).date() >= start and (element['date_created']).date() <= end:
            if element['category'] in dict:
                dict[element['category']] += float(element['value'])
            elif element['category'] not in dict:
                dict[element['category']] = float(element['value'])
            else :
                pass

    for element in dict:
        dict[element] = round(dict[element],2)
        
    return dict
        
    
