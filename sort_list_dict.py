from pprint import pprint


data = [{'date': '2019-08-21', 'weekday': 'Wednesday', 'list':['A', 'B', 'C']},
        {'date': '2019-01-03', 'weekday': 'Thursday', 'list':['A', 'B', 'C']},
        {'date': '2019-01-02', 'weekday': 'Wednesday', 'list':['A', 'B', 'C']},
        {'date': '2019-01-01', 'weekday': 'Tuesday', 'list':['A', 'B', 'C']},
        {'date': '2019-08-19', 'weekday': 'Monday', 'list':['A', 'B', 'C']},
        {'date': '2018-11-01', 'weekday': 'Thursday', 'list':['A', 'B', 'C']}]

sorted_data = sorted(data, key=lambda d: d['date'])
pprint(sorted_data)
