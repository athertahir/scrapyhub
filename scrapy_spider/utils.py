import re


def get_company_name(scraped_data):
    filters = [" \( ", " "]
    for filter in filters:
        postion=re.split(filter, scraped_data, flags=re.IGNORECASE)
        if len(postion) > 1 :
            return postion[0]
    return scraped_data


def get_position(scraped_data):
    filters = [" is hiring ", " wants ", " looking "]
    for filter in filters:
        postion=re.split(filter, scraped_data, flags=re.IGNORECASE)
        if len(postion) > 1 :
            return  re.split(" in ", postion[1].replace('a ', ''), flags=re.IGNORECASE)[0]
    return scraped_data

def get_location(scraped_data):
    filters = [" in "]
    for filter in filters:
        postion=re.split(filter, scraped_data, flags=re.IGNORECASE)
        if len(postion) > 1 :
            return postion[1]
    return ""