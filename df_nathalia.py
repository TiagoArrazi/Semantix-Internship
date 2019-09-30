import pandas as pd

json_mock = {'features': [{'properties': {'i1_isocode': 'SP'}}]}

data = {'Estado': list(),
        'Cidade': list(),
        'País': list()}

df_output = pd.Dataframe()

# list_isocode = [[d['features'][0]['properties']['i1_isocode']
#                  for d in pa.get('{}'.format(i))]
#                 for i in range(df_output.shape[0])
#                 ]
#
# list_i2_name = [[d['features'][0]['properties']['i2_name']
#                  for d in pa.get('{}'.format(i))]
#                 for i in range(df_output.shape[0])]
#
# list_i0_name = [[d['features'][0]['properties']['i0_name']
#                  for d in pa.get('{}'.format(i))]
#                 for i in range(df_output.shape[0])]

list_isocode = list()
list_i2_name = list()
list_i0_name = list()

for i in range(df_output.shape[0]):
    resp = pa.get('{}'.format(i)).json()
    list_isocode.append(resp['features'][0]['properties']['i1_isocode'])
    list_i2_name.append(resp['features'][0]['properties']['i2_name'])
    list_i0_name.append(resp['features'][0]['properties']['i0_name'])


df['Estado'] = list_isocode
df['Cidade'] = list_i2_name
df['País'] = list_i0_name
