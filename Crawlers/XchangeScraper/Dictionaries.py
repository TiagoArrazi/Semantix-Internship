def getCombinationID(combKey):

    combDict = {'usd-eur': 2124, 'usd-jpy': 3 , 'usd-gbp': 2126, 'usd-chf': 4, 'usd-zar': 17, 'usd-aud': 2091, 'usd-brl': 2103,
                'eur-usd': 1, 'eur-jpy': 9, 'eur-gbp': 6, 'eur-chf': 10, 'eur-zar': 100, 'eur-aud': 15, 'eur-brl': 1617,
                'jpy-usd': 1910, 'jpy-eur': 1895, 'jpy-gbp': 1896, 'jpy-chf': 1892, 'jpy-zar': 1911, 'jpy-aud': 1889, 'jpy-brl': 1890,
                'gbp-usd': 2, 'gbp-eur': 1751, 'gbp-jpy': 11, 'gbp-chf': 12, 'gbp-zar': 96, 'gbp-aud': 53, 'gbp-brl': 1736,
                'chf-usd': 1560, 'chf-eur': 1547, 'chf-jpy': 13, 'chf-gbp': 1548, 'chf-zar': 123, 'chf-aud': 1542, 'chf-brl': 1544,
                'zar-usd': 10441, 'zar-eur': 10414, 'zar-jpy': 78, 'zar-gbp': 10415, 'zar-chf': 10409, 'zar-aud': 10404, 'zar-brl': 10407,
                'aud-usd': 5, 'aud-eur': 1487, 'aud-jpy': 49, 'aud-gbp': 1489, 'aud-chf': 48, 'aud-zar': 122, 'aud-brl': 1485,
                'brl-usd': 1516, 'brl-eur': 9419, 'brl-jpy': 1513, 'brl-gbp': 9420, 'brl-chf': 1508, 'brl-zar': 9456, 'brl-aud': 1506}

    return combDict[combKey]

