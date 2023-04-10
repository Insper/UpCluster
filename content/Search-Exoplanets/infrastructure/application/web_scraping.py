#!/usr/bin/env python3
import pandas as pd
import requests
from bs4 import BeautifulSoup
from os import listdir
import io


def file_get(TIC):
   url = "https://exofop.ipac.caltech.edu/tess/target.php?id="+str(TIC)
   page = requests.get(url)
   data= page.text
   soup = BeautifulSoup(data, 'html.parser')
   x=[[link.get('href'), link.get_text()] for link in soup.find_all('a')]
   df = pd.DataFrame(x, columns = ['url', 'text']) 
   df=df.dropna(how='any')
   df=df[df['url'].str.contains("get_file")]
   for substring_1 in file_substring:
      df=df[df['text'].str.contains(substring_1)]
   return df

def file_get_new(TIC):
   TIC_url="https://exofop.ipac.caltech.edu/tess/download_filelist.php?id="+str(TIC)
   test=requests.get(TIC_url)
   return pd.read_csv(io.StringIO(test.text), sep='|')



def bulk_download(obs_type, file_dir=".", user=None, file_substring=[".tbl"], file_search_dict={}, file_ext=None):
   for item in file_search_dict:
      file_search_dict[item]=file_search_dict[item].split('|')
   print(file_search_dict)
   #quit()
   existing_files=listdir(file_dir)
   page_term=None
   if obs_type.lower()[0]=="i": page_term="imaging"
   if obs_type.lower()[0]=="s": page_term="spect"
   if obs_type.lower()[0]=="t": page_term="tseries"
   if not page_term:
      print("Not a valid category of observations")
      quit()
   source_file="https://exofop.ipac.caltech.edu/tess/download_"+page_term+".php?sort=id&output=pipe"
   print(source_file)
   obs_df=pd.read_csv(source_file, sep='|')
   if user:
      obs_df=obs_df[obs_df['User'].str.contains(user)]
   if verbose: print(obs_df)
   observed_TOIs=obs_df['TIC ID'].values
   observed_TIC_list=list(dict.fromkeys(observed_TOIs))
   if verbose: print(observed_TIC_list, len(observed_TIC_list))
   print("%.0f TOIs observed" % len(observed_TIC_list))

   already_downloaded=0
   downloads=0
   download_list=[]
   for TIC in observed_TIC_list:
      test_df=file_get_new(TIC)
      resposta = requests.post("http://192.168.50.10:8080/memq/server/queues/Lista/enqueue/",str(TIC))
      print(resposta.text)
if __name__ == '__main__':
   verbose=False
   #verbose=True
   obs_type="Imaging" #Imaging, Spectroscopy, Time Series
   file_dir="output" #location to save files and check for previous files
   user="ciardi" # user that has uploaded the files being searched for
   file_substring=[".tbl", "-dc"] # substrings to search for in filenames
   #Type, File Name, TIC (not recommended), TOI (not recommended), Date, User, Group, Tag (number only), Description 
   file_search_dict={"User":"ciardi", "File Name": ".tbl|-dc"}
   file_search_dict={"User":"ciardi", "File Name": ".tbl"}
   file_search_dict={"User":"ciardi", "File Name": ".fits"}
   file_search_dict={"User":"ciardi", "File Name": "TOI|_plot", "Type":"Image"}
   file_ext=".fits"
   file_substring=["_plot", "-dc"] # substrings to search for in filenames
   file_ext=".jpg"
   #print(search_dict)
   #quit()
   bulk_download(obs_type, file_dir, user=user, file_substring=file_substring, file_search_dict=file_search_dict, file_ext=file_ext)
