<p align="center">
  <img src="logo.png">
</p>

# CodeFirstGirls Beginners Python

# Homework: Session 5

Topics in this session:

1. Files
1. Pip package manager
1. APIs

Additional resources:

- Requests <https://realpython.com/python-requests/>

- Requests official documentation <https://2.python-requests.org/en/master/>

- Pip <https://realpython.com/what-is-pip/>

- PyPI <https://pypi.org/>

# Task 1

You're having coffee/tea/beverage of your choice with a friend that is learning to program in Python. They're curious about why they would use pip. 

Explain what pip is and one benefit of using pip.

# Task 2

This program should save my data to a file, but it doesn't work when I run it. What is the problem and how do I fix it?

```python
poem = 'I like Python and I am not very good at poems'

with open('poem.txt', 'r') as poem_file:
    poem_file.write(poem)
```