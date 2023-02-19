import requests

def html_to_file(url: str, file:str):
    data = requests.get(url=url).text
    with open(file, 'w') as f:
        f.write(data)

url = 'https://kubernetes.io/docs/concepts/_print/'

file_name = 'concepts.txt'
base_dir = './cache/'
full_file_location = base_dir + file_name

print(f"Getting data from {url} and writing to {full_file_location}")
html_to_file(url,full_file_location)
print('Finished writing data')