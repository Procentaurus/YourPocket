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

def createPeriodData(data, start, end, option):
    dict = {}
    
    if option == "this" or option == "last":

        dict["{}-{}".format(start.year,start.month)] = 0
        for element in data:
            if (element['date_created']).date() >= start and (element['date_created']).date() <= end:
                dict["{}-{}".format(start.year,start.month)] += float(element['value'])

    elif option == "last3":
        startDate = start
        for _ in range(3):
            dict["{1}-{0}".format(startDate.year,startDate.month)] = 0
            if startDate.month >= 12:
                startDate = datetime.date(startDate.year + 1, 1, startDate.day)
            else:
                startDate = datetime.date(startDate.year,startDate.month + 1, startDate.day)
        for element in data:
            if (element['date_created']).date() >= start and (element['date_created']).date() <= end:
                dict["{1}-{0}".format(element["date_created"].date().year, element["date_created"].date().month)] += float(element['value'])

    elif option == "lasty":
        pass
    elif option == "all":
        pass

    return dict
    
