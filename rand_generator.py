import requests
def ran_list_generator(n,min_n=1,max_n=255):
    url =  "https://www.random.org/integers/?num={num}&min={min_n}&max={max_n}&col=1&base=10&format=plain&rnd=new".format(num=str(n),min_n=str(min_n),max_n=str(max_n))
    value = requests.get(url)
    return map(int, value.content.splitlines())

print ran_list_generator(2)