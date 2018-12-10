def getCryptoId(crypto_key):

    crypto_dict = {'bitcoin':1057391, 'ripple':1057392, 'ethereum':1061443, 'bitcoin-cash':1061410, 'stellar':1061451, 
                   'eos':1061444, 'litecoin':1061445, 'tether':1061453, 'cardano':1062537, 'monero':1061467,
                   'tron':1061450, 'iota':1061449, 'dash':1061456, 'binance-coin':16061448, 'nem':1061476, 
                   'neo':1061409, 'ethereum-classic':1057275, 'tezos':1061796, 'zcash':1061465, 'bitcoin-gold':1061452,
                   'vechain':1061537, 'maker':1061538, 'ontology':1072990, 'omisego':1061446}

    return crypto_dict[crypto_key]
