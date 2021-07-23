from bs4 import BeautifulSoup
import lxml
import xml.etree.ElementTree as ET
import time
# Local Files
import dictCreator


xml_file = "data-file.xml"
with open(xml_file, "r", encoding="utf8") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, "lxml")

    items = soup.find_all("e:resource")
    items2 = soup.find_all("e:resource")[2]

newlist = items[1:-1]

data_list_dicts = [
    
]



for item in newlist:
    # print(newlist.index(item))
    if item['type'] == 'component':
        print('component found')
    else:
        search_phrase = item.text.strip()
        
        search_phrase_id = item['id']
      
        if not data_list_dicts:
            print("List is empty")            
            dictCreator.createDict(item, data_list_dicts)     

        else:
        
            list_values = [list(dict_i.values())[0] for dict_i in data_list_dicts]
            list_keys = [list(dict_i.keys())[0] for dict_i in data_list_dicts]
            if search_phrase in list_values:
                value_index = list_values.index(search_phrase)
                key = list_keys[value_index]
                existing_id = key
                print('Repeated:', '*'+search_phrase)
                print(search_phrase_id, 'first occurred at', existing_id)
                
                    # for existing_item_id, existing_item_text in dict_i.items():                     
                    #     if existing_item_text == search_phrase:                        
                    #         existing_id = existing_item_id
                    #         print(existing_id)
            else:  
                print('Unrepeated:', '\/'+search_phrase)                  
                dict = {}
                item_id = item['id']
                dict[item_id] = item.text.strip()
                if dict not in data_list_dicts:  
                    data_list_dicts.append(dict)
    print('Please wait.....')        
    time.sleep(2)        
     
                    
         
      
print(data_list_dicts)



