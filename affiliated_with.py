# -*- coding: utf-8 -*-
## Clean affiliated with data to remove duplicate edges
#62,691,989 combinations before hand

import pandas as pn

# Import data
#csvin = pn.read_csv('PaperAuthorAffiliations.txt', delimiter ='\t')
csvin = pn.read_csv('PaperAuthorAffiliations.txt', delimiter ='\t', dtype='str')
csvin = csvin.drop(csvin.columns[[0, 3, 4, 5]], axis=1)

## Rename columns
csvin.columns =['AuthorID','AffiliationID']

#csvin['AuthorID']=csvin['AuthorID'].astype('object')
#csvin['AffiliationID']=csvin['AffiliationID'].astype('object')

## Drop rows with no values
csvin = csvin.dropna()


## Concatenate columns
csvin['START_ID:(AuthorAffiliation)']=csvin['AuthorID'].map(str)+ csvin['AffiliationID'].map(str)
csvin = csvin.drop('AuthorID',axis=1)

## remove duplicates
csvin = csvin.drop_duplicates()

# rename columns
csvin.columns =[':END_ID(Affiliation)',':START_ID(AuthorAffiliation)']

# output data
csvin.to_csv('affiliated_with.csv', sep='\t', header=True, index=False, index_label=None, mode='w', encoding='utf-8', quoting=None, line_terminator='\n', doublequote=True, escapechar=None, decimal='.')
