

```python
# 1. Write a function that reports the number of sequences in a fasta file
```


```python
import os
os.chdir("/Users/ruijuanli/Desktop/2018_summer/Pithon_Ruijuan.L/Chapter_6/")

fa_file = 'SP1.fa'

def fa_len(fa_file):
    with open(fa_file) as f:
        line_count = 0
        for line in f:
            if line.startswith('>'):
                line_count = line_count + 1
    return(line_count) # can be problematic because sometimes seq can run across several lines 

fa_len(fa_file)
```




    250




```python
# 2. Write a function that reports the number of sequences in a fastq file
```


```python
import re
def fq_len(fq_file):
    with open(fa_file) as f:
        line_count = 0
        for line in f:
            line_count = line_count + 1
    return(round(line_count/4))
```


```python
fq_len("SP1.fq")
```




    125




```python
# 3. Modify one of your functions from problem 1 or 2 to work with a file stored on the internet. For example be able to load this file sample.fa
```


```python
import urllib.request

u = 'http://molb7621.github.io/workshop/_downloads/sample.fa'
f = urllib.request.urlopen(u)
contents = f.read().decode("utf-8", "ignore")
fa_file = print(contents)
fa_file
```

    >derice
    ACTGACTAGCTAGCTAACTG
    >sanka
    GCATCGTAGCTAGCTACGAT
    >junior
    CATCGATCGTACGTACGTAG
    >yul
    ATCGATCGATCGTACGATCG



```python
def fa_len_url(site):
    u = site
    f = urllib.request.urlopen(u)
    fa_file = f.read().decode("utf-8", "ignore")
    line_count = 0
    for line in fa_file:
        if line.startswith('>'):
            line_count = line_count + 1
    return(line_count) # can be problematic because sometimes seq can run across several lines 

```


```python
site = 'http://molb7621.github.io/workshop/_downloads/sample.fa'
fa_len_url(site)
```




    4




```python
# 4. Write a function that converts a fastq file to a fasta file
```


```python
with open('SP1.fq', 'r') as f:
    count = 0
    for line in f:
        count+=1
        if count % 2 == 0: # will learn this tomorrow... 
            print(line) 
```


      File "<ipython-input-23-ef939e06b932>", line 5
        if count % 2 == 0 and count % 3 != 0: #this is the remainder operator
                                                                             ^
    SyntaxError: unexpected EOF while parsing




```python
# 5. Create an instance of your 'Organism' class from last week. Demonstrate pickling it to a file, and loading it from the file. Note: when opening the file you may need to add the 'b' option
```


```python
os.chdir("/Users/ruijuanli/Desktop/2018_summer/Pithon_Ruijuan.L/Chapter_5/")
```


```python
from Problem_2 import Organism
plant1 = ('Plantae', 'Tracheophyta', 'Magnoliopsida', 'Brassicales',
         'Brassicaceae', 'Brassica', 'Napus', 'DaAe')
```


```python
A = Organism(*plant1) # unpacking tuples 
```


```python
import pickle
file = A.short() 
```

    DaAe's short name description:
    Brassica napus



```python
file # I don't know how to save the item to an object 
```
