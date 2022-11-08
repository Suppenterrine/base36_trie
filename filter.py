# import pandas as pd
# pandas
# df = pd.DataFrame(list)
# print(df.head())
# df = df[df.id==5]

data = [
    {
        'id': 0,
        '0': [
            {
                'id': '00',
                '0': [
                    {
                        'id': '000',
                        '0': 0
                    },
                    {
                        'id': '001',
                        '1': 1
                    }
                ]
            },
            {'id': '01', '1': [{'id': '010', '0': 0}, {'id': '011', '1': 1}]}, {'id': '02', '2': [{'id': '020', '0': 0}, {'id': '021', '1': 1}]}, {'id': '03', '3': [{'id': '030', '0': 0}, {'id': '031', '1': 1}]}, {'id': '04', '4': [{'id': '040', '0': 0}, {'id': '041', '1': 1}]}]
    },
    {
        'id': 1,
        '1': [
            {
                'id': '10',
                '0': [
                    {
                        'id': '100',
                        '0': 0
                    },
                    {
                        'id': '101',
                        '1': 1
                    }
                ]
            }, {'id': '11', '1': [{'id': '110', '0': 0}, {'id': '111', '1': 1}]}, {'id': '12', '2': [{'id': '120', '0': 0}, {'id': '121', '1': 1}]}, {'id': '13', '3': [{'id': '130', '0': 0}, {'id': '131', '1': 1}]}, {'id': '14', '4': [{'id': '140', '0': 0}, {'id': '141', '1': 1}]}]}, {'id': 2, '2': [{'id': '20', '0': [{'id': '200', '0': 0}, {'id': '201', '1': 1}]}, {'id': '21', '1': [{'id': '210', '0': 0}, {'id': '211', '1': 1}]}, {'id': '22', '2': [{'id': '220', '0': 0}, {'id': '221', '1': 1}]}, {'id': '23', '3': [{'id': '230', '0': 0}, {'id': '231', '1': 1}]}, {'id': '24', '4': [{'id': '240', '0': 0}, {'id': '241', '1': 1}]}]}, {'id': 3, '3': [{'id': '30', '0': [{'id': '300', '0': 0}, {'id': '301', '1': 1}]}, {'id': '31', '1': [{'id': '310', '0': 0}, {'id': '311', '1': 1}]}, {'id': '32', '2': [{'id': '320', '0': 0}, {'id': '321', '1': 1}]}, {'id': '33', '3': [{'id': '330', '0': 0}, {'id': '331', '1': 1}]}, {'id': '34', '4': [{'id': '340', '0': 0}, {'id': '341', '1': 1}]}]}, {'id': 4, '4': [{'id': '40', '0': [{'id': '400', '0': 0}, {'id': '401', '1': 1}]}, {'id': '41', '1': [{'id': '410', '0': 0}, {'id': '411', '1': 1}]}, {'id': '42', '2': [{'id': '420', '0': 0}, {'id': '421', '1': 1}]}, {'id': '43', '3': [{'id': '430', '0': 0}, {'id': '431', '1': 1}]}, {'id': '44', '4': [{'id': '440', '0': 0}, {'id': '441', '1': 1}]}]}, {'id': 5, '5': [{'id': '50', '0': [{'id': '500', '0': 0}, {'id': '501', '1': 1}]}, {'id': '51', '1': [{'id': '510', '0': 0}, {'id': '511', '1': 1}]}, {'id': '52', '2': [{'id': '520', '0': 0}, {'id': '521', '1': 1}]}, {'id': '53', '3': [{'id': '530', '0': 0}, {'id': '531', '1': 1}]}, {'id': '54', '4': [{'id': '540', '0': 0}, {'id': '541', '1': 1}]}]}, {'id': 6, '6': [{'id': '60', '0': [{'id': '600', '0': 0}, {'id': '601', '1': 1}]}, {'id': '61', '1': [{'id': '610', '0': 0}, {'id': '611', '1': 1}]}, {'id': '62', '2': [{'id': '620', '0': 0}, {'id': '621', '1': 1}]}, {'id': '63', '3': [{'id': '630', '0': 0}, {'id': '631', '1': 1}]}, {'id': '64', '4': [{'id': '640', '0': 0}, {'id': '641', '1': 1}]}]}, {'id': 7, '7': [{'id': '70', '0': [{'id': '700', '0': 0}, {'id': '701', '1': 1}]}, {'id': '71', '1': [{'id': '710', '0': 0}, {'id': '711', '1': 1}]}, {'id': '72', '2': [{'id': '720', '0': 0}, {'id': '721', '1': 1}]}, {'id': '73', '3': [{'id': '730', '0': 0}, {'id': '731', '1': 1}]}, {'id': '74', '4': [{'id': '740', '0': 0}, {'id': '741', '1': 1}]}]}, {'id': 8, '8': [{'id': '80', '0': [{'id': '800', '0': 0}, {'id': '801', '1': 1}]}, {'id': '81', '1': [{'id': '810', '0': 0}, {'id': '811', '1': 1}]}, {'id': '82', '2': [{'id': '820', '0': 0}, {'id': '821', '1': 1}]}, {'id': '83', '3': [{'id': '830', '0': 0}, {'id': '831', '1': 1}]}, {'id': '84', '4': [{'id': '840', '0': 0}, {'id': '841', '1': 1}]}]}, {'id': 9, '9': [{'id': '90', '0': [{'id': '900', '0': 0}, {'id': '901', '1': 1}]}, {'id': '91', '1': [{'id': '910', '0': 0}, {'id': '911', '1': 1}]}, {'id': '92', '2': [{'id': '920', '0': 0}, {'id': '921', '1': 1}]}, {'id': '93', '3': [{'id': '930', '0': 0}, {'id': '931', '1': 1}]}, {'id': '94', '4': [{'id': '940', '0': 0}, {'id': '941', '1': 1}]}]}]


# [query1] = list(filter(lambda m : m[0]['id']==0, data ))
print(
    data[1]['id']
)