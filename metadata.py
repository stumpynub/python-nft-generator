def create_metadata(name : str, description : str, id : int, url): 
    meta_data_dict = {  "url" : url,
                        "name" : name, 
                        "description" : description, 
                        "id" : id   } 

    return meta_data_dict
