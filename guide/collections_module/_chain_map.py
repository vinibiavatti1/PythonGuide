"""
Chain Map

* Dict-like class for creating a single view of multiple mappings
* A ChainMap groups multiple dicts or other mappings together to create a
  single, updateable view. If no maps are specified, a single empty dictionary
  is provided so that a new chain always has at least one mapping

* Syntax
  * ChainMap(*maps)
"""
import collections


# Chain Map
dct1 = {'name': ' Vini', 'age': 26}
dct2 = {'name': ' Ana', 'country': 'Portugal'}
dct_chain = collections.ChainMap(dct1, dct2)
print(dct_chain)
# ChainMap({'name': ' Vini', 'age': 26},
# {'name': ' Ana', 'country': 'Portugal'})


# List cast
dct1 = {'name': 'Vini', 'age': 26}
dct2 = {'name': 'Ana', 'country': 'Portugal'}
dct_chain = collections.ChainMap(dct1, dct2)
print(list(dct_chain))
# ['name', 'country', 'age']


# Maps
# * A user updateable list of mappings. The list is ordered from first-searched
#   to last-searched
dct1 = {'name': 'Vini', 'age': 26}
dct2 = {'name': 'Ana', 'country': 'Portugal'}
dct_chain = collections.ChainMap(dct1, dct2)
print(dct_chain.maps)
# [{'name': ' Vini', 'age': 26}, {'name': ' Ana', 'country': 'Portugal'}]


# New Child
# * Returns a new ChainMap containing a new map followed by all of the maps in
#   the current instance
dct1 = {'name': 'Vini', 'age': 26}
dct2 = {'name': 'Ana', 'country': 'Portugal'}
dct3 = {'name': 'Ze', 'profession': {'name': 'PO'}}
dct_chain = collections.ChainMap(dct1, dct2)
dct_chain = dct_chain.new_child(dct3)
print(dct_chain)
# ChainMap({'name': 'Ze', 'profession': {'name': 'PO'}},
# {'name': 'Vini', 'age': 26}, {'name': 'Ana', 'country': 'Portugal'})


# Parents
# * Property returning a new ChainMap containing all of the maps in the current
#   instance except the first one
dct1 = {'name': 'Vini', 'age': 26}
dct2 = {'name': 'Ana', 'country': 'Portugal'}
dct_chain = collections.ChainMap(dct1, dct2)
print(dct_chain.parents)
# ChainMap({'name': 'Ana', 'country': 'Portugal'})
