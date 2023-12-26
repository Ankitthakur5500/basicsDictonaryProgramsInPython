#Python – Insertion at the beginning in OrderedDict
from collections import OrderedDict
original_dict = OrderedDict([('a','1'), ('b','2')])
original_dict.update({'c':'3'})
original_dict.move_to_end('c', last=False)
print(original_dict)
