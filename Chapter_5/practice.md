

```python
### 1. On the python website, find a builtin module. Describe and show examples of some of the useful functions in the module and how they might be utilized by us.
```


```python
import re # regular expression 
my_string = 'This is my string which contains words and numbers like 123'
new_string = re.search('words', my_string)
new_string.group() # the matching text 
```




    'words'




```python
print(new_string.group())
```

    words



```python
# Start and end in the string

start = new_string.start()
end = new_string.end()
print(my_string[start:end])
```

    words



```python
# Match ambiguous strings next two words after 'my'

new_string = re.search('my \w+ \w+', my_string)
print(new_string.group())
```

    my string which



```python
# Find all words which end in 's' in a string

s = re.findall('\w+s', my_string)
print(s)
```

    ['This', 'is', 'contains', 'words', 'numbers']



```python
# Replace characters with new characters

new_string = re.sub(' ', '\n' , my_string)
new_string
print(new_string)
```

    This
    is
    my
    string
    which
    contains
    words
    and
    numbers
    like
    123



```python
# Count occurences of substitutions

new_string = re.subn(' ', '\n' , my_string)
new_string
print(new_string[1])
```

    10



```python
### 2. Write a class called "Organism". Have the class initialize with the organism's complete taxonomic lineage (KPCOFGS) and common name. Write methods which allow a user to see these values in informative ways.
```


```python
class Organism:
    def __init__(self,
                 K = '??',
                 P = '??',
                 C = '??',
                 O = '??',
                 F = '??',
                 G = '??',
                 S = '??',
                 N = '??'):
        self.K = K
        self.P = P
        self.C = C
        self.O = O
        self.F = F
        self.G = G
        self.S = S
        self.N = N
        for i in self.__dict__.keys(): # ? 
            if self.__dict__[i] == '??':
                 print('No value provided for: ', i)

    def description(self): # ? 
        print('Access the lineage values of the organism using the first \
letters in\nKingdom, Phylum, Class, Order, Family, Genus, Species, and Name \
(KPCOFGSN)\nLonger descriptions can also be accessed.\n\
Examples: object.K, object.full(), and object.short()')

    def full(self): # method? 
        print(self.N, '\'s full name description:\n',
              'Kingdom = ', self.K, "\n",
              'Phylum = ', self.P, "\n",
              'Class = ', self.C, "\n",
              'Order = ', self.O, "\n",
              'Family = ', self.F, "\n",
              'Genus = ', self.G, "\n",
              'Species = ', self.S, sep = "")

    def short(self):
        print(self.N, '\'s short name description:\n',
              self.G, ' ', self.S.lower(), sep = "")
```


```python
### Problem 3 Demonstrate inheritance by importing your class "Organism" from problem 2. Use it to create a new class called "LongOrganism" which inherits "Organism" and modifies it by adding any other attributes that may be significant about an organism (ie ploidy, genome size, region). Write new methods which allow a user to see these values in informative ways.
```


```python
import os

os.chdir("/Users/ruijuanli/Desktop/2018_summer/Pithon_Ruijuan.L/Chapter_5/")
```


```python
from Problem_2 import Organism

print('This module allows you to create an organism class. It expects Kingdom\
 Phylum, Class, Order, Family, Genus, Species, Common Name, Region, Size, and \
Ploidy in that order')
      
class LongOrganism(Organism): # inherit? 
    def __init__(self,
                 K = '??',
                 P = '??',
                 C = '??',
                 O = '??',
                 F = '??',
                 G = '??',
                 S = '??',
                 N = '??',
                 Region = '??',
                 Size = '??',
                 Ploidy = '??'):
        self.Region = Region
        try: ### don't understand 
            self.Ploidy = int(Ploidy)
        except ValueError:
            self.Ploidy = Ploidy
            print('Ploidy must be numeric')
        try:
            self.Size = int(Size)
        except ValueError:
            self.Size = Size
            print('Size must be numeric and is in Mb')
        Organism.__init__(self,K,P,C,O,F,G,S,N) # why this? 

    def genome(self): # new method to see genome ploidy level and size 
        print(self.N, '\'s genome description:\n',
              'Ploidy = ', self.Ploidy, 'n\n',
              'Genome Size = ', self.Size, ' Mb', sep = '')

    def region(self): # new method to see region, what is region 
        print(self.N, '\'s region description:\n',
              'Region = ', self.Region, sep = '')

        
    def full(self):
        Organism.full(self) # ??? 
        self.genome()
        self.region()

    def description(self):
        Organism.description(self)
        print('Genome information can be acccessed using\n',
              'object.genome(), object.Ploidy and object.Size\n',
              'Region information can be acccessed using\n',
              'object.region() and object.Region', sep = '')
```

    This module allows you to create an organism class. It expects Kingdom Phylum, Class, Order, Family, Genus, Species, Common Name, Region, Size, and Ploidy in that order



```python
### Problem 4 Write a function which allows a user to compare and/or contrast two instances of your class "LongOrganism"
```


```python
def OrganismCompare(organism1, organism2, comparison = 'full'):
    name1 = type(organism1).__name__ # ????
    name2 = type(organism2).__name__
    if name1 != 'LongOrganism' or name2 != 'LongOrganism':
        print('One of the two input organisms was not of class LongOrganism')
        return

    if comparison == 'lineage' or comparison == 'full':
        lines = ['K','P','C','O','F','G','S','N']
        lines_dict = {'K' : 'kingdom', 'P' : 'phylum',
                     'C' : 'class', 'O' : 'order',
                     'F' : 'family', 'G' : 'genus',
                     'S' : 'species', 'N' : 'name'}
        same = ''
        i = 0
        while i < len(lines):
            if getattr(organism1, lines[i]) != getattr(organism2, lines[i]):
                break
            i += 1
        if i == 0:
            print(organism1.N, 'and', organism2.N, 'belong to different kingdoms')
        elif i == len(lines):
            print(organism1.N, 'and', organism2.N, 'are the same')
        elif i == len(lines) - 1:
            print(organism1.N, 'and', organism2.N, 'are the same species with different names')
        else:
            print(organism1.N, 'and', organism2.N, 'share the same', end = ' ')
            for x in range(i):
                if x != i - 1:
                    print(lines_dict.get(lines[x]), end = ', ')
                else:
                    print('and ', lines_dict.get(lines[x]), '.', sep = '')

    if comparison == 'genetic' or comparison == 'full':
        if organism1.Ploidy == organism2.Ploidy:
            print(organism1.N, ' and ',
                  organism2.N, ' have the same ploidy: ',
                  organism1.Ploidy, 'n', sep = '')
        else:
            print(organism1.N, 'and', organism2.N, 'have different ploidy')
            print(organism1.N, ' has a ploidy of ',
                  organism1.Ploidy, 'n', sep = '')
            print(organism2.N, ' has a ploidy of ',
                  organism2.Ploidy, 'n', sep = '')
        if organism1.Size == organism2.Size:
            print(organism1.N, ' and ', organism2.N,
                  ' have the same genome size: ',
                  organism1.Size, 'Mb', sep = '')
        else:
            if organism1.Size > organism2.Size:
                print(organism1.N, ' has a genome size of ',
                      organism1.Size, 'Mb which is greater than ',
                      organism2.N, '\'s genome size of ', organism2.Size,
                      'Mb.', sep = '')
            else:
                print(organism2.N, ' has a genome size of ',
                      organism2.Size, 'Mb which is greater than ',
                      organism1.N, '\'s genome size of ', organism1.Size,
                      'Mb.', sep = '')
    if comparison == 'region' or comparison == 'full':
        if organism1.Region == organism2.Region:
            print(organism1.N, 'and', organism2.N, 'have the same region:',
                  organism1.Region)
        else:
            print(organism1.N, 'and', organism2.N,
                  ' have the different regions,', organism1.N,
                  'is from', organism1.Region, 'while', organism2.N,
                  'is from', organism2.Region)
    return
```


```python
### Problem 5 Import your class and function from problems 3 and 4. Demonstrate using them together
```


```python
from Problem_3 import LongOrganism
from Problem_4 import OrganismCompare

plant1 = ('Plantae', 'Tracheophyta', 'Magnoliopsida', 'Brassicales',
         'Brassicaceae', 'Brassica', 'Napus', 'DaAe', 'Asia', 1120, 4)

plant2 = ('Plantae', 'Tracheophyta', 'Magnoliopsida', 'Brassicales',
         'Brassicaceae', 'Brassica', 'Napus', 'DaOl', 'Asia', 1120, 4)

plant3 = ('Plantae', 'Tracheophyta', 'Magnoliopsida', 'Brassicales',
         'Brassicaceae', 'Brassica', 'Rapa', 'Rapa', 'Asia', 485, 2)
```


```python
A = LongOrganism(*plant1) # why *, unpacking tuples 
B = LongOrganism(*plant2)
C = LongOrganism(*plant3)

print() # why print? 
```

    



```python
print('Looking at organism A')
A.full() # full method 
```

    Looking at organism A
    DaAe's full name description:
    Kingdom = Plantae
    Phylum = Tracheophyta
    Class = Magnoliopsida
    Order = Brassicales
    Family = Brassicaceae
    Genus = Brassica
    Species = Napus
    DaAe's genome description:
    Ploidy = 4n
    Genome Size = 1120 Mb
    DaAe's region description:
    Region = Asia



```python
print()
```

    



```python
print('Looking at organism C')
C.full()

print()
```

    Looking at organism C
    Rapa's full name description:
    Kingdom = Plantae
    Phylum = Tracheophyta
    Class = Magnoliopsida
    Order = Brassicales
    Family = Brassicaceae
    Genus = Brassica
    Species = Rapa
    Rapa's genome description:
    Ploidy = 2n
    Genome Size = 485 Mb
    Rapa's region description:
    Region = Asia
    



```python
print('Compare all between A and C')
OrganismCompare(A, C)
```

    Compare all between A and C
    DaAe and Rapa share the same kingdom, phylum, class, order, family, and genus.
    DaAe and Rapa have different ploidy
    DaAe has a ploidy of 4n
    Rapa has a ploidy of 2n
    DaAe has a genome size of 1120Mb which is greater than Rapa's genome size of 485Mb.
    DaAe and Rapa have the same region: Asia



```python
print('Compare lineages of A and B')
OrganismCompare(A, B, 'lineage')  
```

    Compare lineages of A and B
    DaAe and DaOl are the same species with different names



```python
print('Compare genetics of B and C')
OrganismCompare(B, C, 'genetic')
```

    Compare genetics of B and C
    DaOl and Rapa have different ploidy
    DaOl has a ploidy of 4n
    Rapa has a ploidy of 2n
    DaOl has a genome size of 1120Mb which is greater than Rapa's genome size of 485Mb.

