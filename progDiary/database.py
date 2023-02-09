'''
This file adds/gets data from the data store
'''

## Data store
entries = []


def add_entry(entry_content, entry_date):
    ## Adding the newly created dictionary to the 'entries' list
    entries.append({"content": entry_content, "date": entry_date})



def get_entries():
    return entries