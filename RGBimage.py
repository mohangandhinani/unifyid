import requests
from PIL import Image
import numpy as np

def array(r, c):
    f_l = []
    for _ in xrange(4):
        URL = "https://www.random.org/integers/?num={num}&min=1&max=255&col=1&base=10&format=plain&rnd=new".format(num=(r / 2) * (c / 2))
        value = requests.get(URL)
        t_l = map(int, value.content.splitlines())
        f_l.extend(t_l)
    to_return = []
    for i in xrange(0, r * c, c):
        to_return.append(f_l[i:i + c])
    return to_return

def image_gen():
    sz = 128
    RGB = np.zeros((sz, sz, 3), 'uint8')
    RGB[..., 0] = array(sz, sz)
    RGB[..., 1] = array(sz, sz)
    RGB[..., 2] = array(sz, sz)
    img = Image.fromarray(RGB)
    img.save('solution.jpeg')
