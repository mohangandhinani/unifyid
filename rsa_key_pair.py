from Crypto.PublicKey import RSA


def RSA_key_pair(bits_len=1024):
    key = RSA.generate(bits_len)  # number of bits
    pub = key.publickey().exportKey("PEM")  # using pem format
    priv = key.exportKey("PEM")
    print "public\n",pub
    print "private\n",priv
    return pub, priv


print RSA_key_pair()
