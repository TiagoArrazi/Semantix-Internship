from collections import namedtuple

def build_aggregation_names(prefix):
    Aggregations = namedtuple('Aggregations', ['aggregation_1', 'aggregation_2'])
    suffix_list = ['_first_agg', '_second_agg']
    return Aggregations._make(['{}{}'.format(prefix, suffix) for suffix in suffix_list])


if __name__ == '__main__':
    aggs = build_aggregation_names('my_prefix')
    print(aggs)
    print(aggs.aggregation_1)
    print(aggs.aggregation_2)
