# jo functions baar-baar use hote hain, unko yaha rakhte hain(utils.py = tools ka dabba (toolbox))

# Example:

# 1. email validation
# 2. password hashing
# 3. date formatting
# 4. calculations
# 5. file handling

import os , sys
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)
       
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)