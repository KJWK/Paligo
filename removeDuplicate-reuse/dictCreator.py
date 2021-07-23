def createDict(item, data_list_dicts):
    dict = {}
    item_id = item['id']
    dict[item_id] = item.text.strip()
    data_list_dicts.append(dict)
    return data_list_dicts



    