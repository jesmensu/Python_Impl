
from collections import OrderedDict

# Creating a iniordered ordered dict
w = OrderedDict()
 
# Initialising ordered_dict
w = OrderedDict([('akshat', '1'), ('nikhil', '2')])

# Inserting new key-value pair at the beginning of w
w.update({'manjeet':'3'})
print(w)
w.move_to_end('manjeet', last = False)

print(w)