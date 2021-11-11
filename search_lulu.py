import requests
from bs4 import BeautifulSoup
import json

class Lululemon:
  def __init__(self):
    self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    self.url = 'https://shop.lululemon.com'
    
  def get_data(self, url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    data = soup.find(text=True)

    parsed = json.loads(data)
    text = json.dumps(parsed, sort_keys=True, indent=4)
    return text

  def scuba(self, preference):
    
    #XS/S
    scuba_url_xss = 'https://shop.lululemon.com/p/womens-outerwear/Scuba-Oversized-12-Zip-Hoodie/_/prod9960807?sz=XS%2FS'
    response = requests.get(scuba_url_xss)
    content = response.content
    soup_xss = BeautifulSoup(content, 'html.parser')
    soup2_xss = soup_xss.find_all(role="radio")
    
    soup_string_xss = str(soup2_xss)
    list_of_colors_xss = []
    i = soup_string_xss.find('<img alt=\"')
    while i != -1:
      j = soup_string_xss.find('\"', i+10)
      list_of_colors_xss.append(soup_string_xss[i+9:j+1])
      i = soup_string_xss.find('<img alt=\"', i+1)

    #M/L
    scuba_url_ml = 'https://shop.lululemon.com/p/womens-outerwear/Scuba-Oversized-12-Zip-Hoodie/_/prod9960807?sz=M%2FL'
    response = requests.get(scuba_url_ml)
    content = response.content
    soup_ml = BeautifulSoup(content, 'html.parser')
    soup2_ml = soup_ml.find_all(role="radio")
    
    soup_string_ml = str(soup2_ml)
    list_of_colors_ml = []
    i = soup_string_ml.find('<img alt=\"')
    while i != -1:
      j = soup_string_ml.find('\"', i+10)
      list_of_colors_ml.append(soup_string_ml[i+9:j+1])
      i = soup_string_ml.find('<img alt=\"', i+1)


    #XL/XXL
    scuba_url_xlxxl = 'https://shop.lululemon.com/p/womens-outerwear/Scuba-Oversized-12-Zip-Hoodie/_/prod9960807?sz=XL%2FXXL'
    response = requests.get(scuba_url_xlxxl)
    content = response.content
    soup_xlxxl = BeautifulSoup(content, 'html.parser')
    soup2_xlxxl = soup_xlxxl.find_all(role="radio")
    
    #print(soup2_xlxxl)

    soup_string_xlxxl = str(soup2_xlxxl)
    list_of_colors_xlxxl = []
    i = soup_string_xlxxl.find('<img alt=\"')
    while i != -1:
      j = soup_string_xlxxl.find('\"', i+10)
      list_of_colors_xlxxl.append(soup_string_xlxxl[i+9:j+1])
      i = soup_string_xlxxl.find('<img alt=\"', i+1)

    scuba_output = ''
    available_colors_xss = []
    number_of_available_colors_xss = 0
    available_colors_ml = []
    number_of_available_colors_ml = 0
    available_colors_xlxxl = []
    number_of_available_colors_xlxxl = 0

    for item in list_of_colors_xss:
      if "not available" in item:
        i += 1
      else:
        number_of_available_colors_xss += 1
        available_colors_xss.append(item[0:])
    
    for item in list_of_colors_ml:
      if "not available" in item:
        i += 1
      else:
        number_of_available_colors_ml += 1
        available_colors_ml.append(item[0:])

    for item in list_of_colors_xlxxl:
      if "not available" in item:
        i += 1
      else:
        number_of_available_colors_xlxxl += 1
        available_colors_xlxxl.append(item[0:])


    scuba_output += "**XS/S:**\n"
    if number_of_available_colors_xss > 0:
      scuba_output += (', '.join(available_colors_xss))
      scuba_output += '\n'
    else:
      scuba_output += ("There are no available colors in this size.\n")
    
    scuba_output += "**M/L:**\n"
    if number_of_available_colors_ml > 0:
      scuba_output += (', '.join(available_colors_ml))
      scuba_output += '\n'
    else:
      scuba_output += ("There are no available colors in this size.\n")

    scuba_output += "**XL/XXL:**\n"
    if number_of_available_colors_xlxxl > 0:
      scuba_output += (', '.join(available_colors_xlxxl))
    else:
      scuba_output += ("There are no available colors in this size.")
    
    scuba_auto_output = ''

    if preference == 1:
      return scuba_output
    else:
      if number_of_available_colors_xss > 0:
        scuba_auto_output += (', '.join(available_colors_xss)) 
      else:
        scuba_auto_output += '0'
      return scuba_auto_output
