from re import sub

data_clickstream={"showcase":"","listingType":"USED","unitTypes":["Casa Padrão"],
                  "constructionStatus":"","listingId":"16443993","listingPosition":"",
                  "areas":["140"],"parkingSpaces":["4"],"bathrooms":"","bedrooms":["2"],
                  "suites":[],"salePrices":[],"rentalPrices":[" 3.000"],"condoFee":"0",
                  "iptuPrices":[" 167"],"businessTypes":["RENTAL"],
                  "address":["Brasil","SP","Sao Paulo","JD DA GLORIA","Rua Doutor Dolzani","29","01546000"],"publisherId":"2648441"}

key_list = list(data_clickstream.keys())

print(data_clickstream)
print('\n')

for key in key_list:

    if isinstance(data_clickstream[key], list):
        
        if len(data_clickstream[key]) == 0:

            data_clickstream[key] = '0'
        
        continue

print('\n')
print(data_clickstream)
