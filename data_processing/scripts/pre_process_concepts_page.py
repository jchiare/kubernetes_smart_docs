import tiktoken
from bs4 import BeautifulSoup
import csv
from clients.openai_client import OpenAIClient
import sys

def num_tokens_from_string(string: str, encoding_model = "text-davinci-003") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_model)
    num_tokens = len(encoding.encode(string))
    return num_tokens        

def skippable_section(next_sibling: str,element_text: str | None):
    
    # skip empty text sections
    if not element_text:
        return True

    # skip h elements
    if next_sibling.name == 'h2' or next_sibling.name == 'h3' or next_sibling.name == 'h4':
        return True
    
    return False              

def get_data_and_write_csv(file_location = './cache/concepts.txt'):
    """
    Recursively find all the pages that are linked to the Wikipedia titles in the list
    """
    
    data = {}
    
    with open(file_location, 'r') as file:

        soup = BeautifulSoup(file, 'html.parser')
        h1_elements = soup.find_all('h1')
  
        for h1 in h1_elements:
            
            # skip h1 element if its the title
            h1_element_class_name = h1.get('class')
            if h1_element_class_name and h1_element_class_name[0] == 'title':
                continue 
            
            # Find the next sibling element after the h1 element
            next_sibling = h1.find_next_sibling()

            last_sub_section = 'default'
            # Loop through all siblings until the next h1 element is reached
            while next_sibling and next_sibling.name != 'h1':
                
                # strips html thanks to beautiful soup
                element_text = next_sibling.get_text().replace('\n','').strip()
                h1_text = h1.get_text()
                
                #skip whats next section
                if element_text.lower() == "what's next" and next_sibling.name == 'h2':
                    # get the next html element sibling and restart the loop
                    next_sibling = next_sibling.find_next_sibling()
                    continue
                
                # check if there is a new sub section 
                is_new_sub_section = next_sibling.name == 'h2' or next_sibling.name == 'h3' or next_sibling.name == 'h4' 
                if is_new_sub_section:
                    last_sub_section = element_text
                
                # add the element text to the sub section
                # and calculate the total tokens
                token_count = num_tokens_from_string(element_text)
                if h1_text in data:
                    if last_sub_section not in data[h1_text]['sections']:
                        data[h1_text]['sections'][last_sub_section] = element_text
                    else:
                        data[h1_text]['sections'][last_sub_section] = data[h1_text]['sections'][last_sub_section] + ' ' + element_text
                    data[h1_text]['total_token_count'] += token_count
                else: 
                    data[h1_text] = {'sections': {last_sub_section:element_text}, 'total_token_count': token_count}
                
                # get the next html element sibling and restart the loop
                next_sibling = next_sibling.find_next_sibling()
    
    return data


# create csv based on the data 
# in the format
# Section, Sub Section, Content, Content Embedding, Token Count
def get_embedding_and_create_csv(data: dict, target_file_name: str):
    with open(target_file_name, 'w', newline='') as file:
        fieldnames = ['Section', 'Sub Section', 'Content', 'Content Embedding', 'Content Token Count']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for key in data.keys():
            # if key == '5 - Workloads' or key == '5.1 - Pods' or key == '5.1.1 - Pod Lifecycle':
                for section_key in data[key]['sections'].keys():
                    content = data[key]['sections'][section_key]
                    section_token_count = num_tokens_from_string(content)
                    
                    # section is likely not useful is less than 40 tokens
                    if section_token_count > 40:
                        content_embedding = OpenAIClient.get_embedding(content)
                        writer.writerow({'Section':key,  'Sub Section': section_key , 'Content':content, 'Content Embedding': content_embedding,'Content Token Count': section_token_count})    



def count_tokens_in_csv_file(target_file_name: str, field = 'Content Token Count'):

    csv.field_size_limit(sys.maxsize)
    with open(target_file_name, 'r', newline='') as file:
        total_tokens = 0  
        csvfile = csv.DictReader(file)
        for line in csvfile:
            total_tokens += int(line[field])
        print(total_tokens)


data = get_data_and_write_csv('./cache/concepts.txt')

target_file_name = 'embedding_result.csv'
get_embedding_and_create_csv(data, target_file_name)

# count_tokens_in_csv_file(target_file_name)
