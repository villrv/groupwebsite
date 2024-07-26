import numpy as np
from pybtex.database.input import bibtex
import json


my_bib_file = 'export-bibtex.bib'


#open a bibtex file
parser = bibtex.Parser()
bibdata = parser.parse_file(my_bib_file)

# NOTE TO ME
'''

There is a bug where 'author' is not showing up -- need to fix to get it to work...

'''

new_json_dict = []
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    print(type(b))
    print(b)
    print(bibdata.entries)
    sys.exit()
    new_json_dict.append(dict(b))
    '''
    try:
        # change these lines to create a SQL insert
        print(b['title'])
        #deal with multiple authors
        for author in bibdata.entries[bib_id].persons["author"]:
            print(author.first(), author.last())
    # field may not exist for a reference
    except(KeyError):
        continue
    '''

with open('bib.json', 'w') as f:
    json.dump(new_json_dict, f)