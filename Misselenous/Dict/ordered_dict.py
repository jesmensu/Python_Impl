
from collections import OrderedDict
 
# Initialising ordered_dict
d = OrderedDict([('akshat', '1'), ('nikhil', '2')])
 
# Creating a iniordered ordered dict
w = OrderedDict()
 
# Inserting new key-value pair at the beginning of w
w.update({'manjeet':'3'})
w.move_to_end('manjeet', last = False)

print(w)