from itertools import chain, starmap
import pandas as pd

def flatten_json_iterative_solution(dictionary):
    

    def unpack(parent_key, parent_value):
        
        
        if isinstance(parent_value, dict):
            for key, value in parent_value.items():
                temp1 = parent_key + '.' + key
                yield temp1, value
        elif isinstance(parent_value, list):
            i = 0 
            for value in parent_value:
                temp2 = parent_key + '.' +str(i) 
                i += 1
                yield temp2, value
        else:
            yield parent_key, parent_value    

            
    
    while True:
        dictionary = dict(chain.from_iterable(starmap(unpack, dictionary.items())))

        if not any(isinstance(value, dict) for value in dictionary.values()) and \
           not any(isinstance(value, list) for value in dictionary.values()):
            break

    return dictionary

test = {
  "event": "click_event", 
  "properties": { 
    "section": "top_nav", 
    "items": [{ 
      "item_id": 12345, 
      "position": 1 
    }, { 
      "item_id": 67890, 
      "position": 2 
    }, { 
      "item_id": 54321, 
      "position": 3 
    }]
  }
}
df = pd.Series(flatten_json_iterative_solution(test)).to_frame()
print(df)

