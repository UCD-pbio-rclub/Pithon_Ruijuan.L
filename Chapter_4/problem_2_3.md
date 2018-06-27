

```python
2) Write a function which takes a sentence as input and returns the reverse order of the words. ie "these are words" --> "words are these". Bonus: Capitalize the the first letter of the first word and end the returned string with the same punctuation as the input string. ie "these are words!" --> "Words are these!"
```


```python
def reverseString(input):
        return input[::-1]
```


```python
reverseString('haha')
```




    'ahah'




```python
3) Write a function which asks the user for a string and prints out whether the string is a palindrome or not
```


```python
def is_palindrom(s):

    # the number of char in s.
    n = len(s)
    # compare the first half of s to the reverse of the second half of s
    # omit the middle character of an odd-length string. 
    return s[:n//2] == reverse(s[n - n//2:])

def reverse(s):
        # Return a reversed version of s.
        rev = ''
        # for each character in s, add that char to the begining of rev.
        for ch in s:
                rev = ch + rev

        return rev
```


```python
is_palindrom('word')
```




    False




```python
is_palindrom('ahha')
```




    True




```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
