# harvest-ql

Harvest QL, a simple poc of a interpreter for sql language for harvest proccess.

## description

This is a only a poc, under a very early stage of development, the idea is to provide a simple interpreter of a language like a minimal and similar subset of SQL for harvest of different type of parser (example web-table), remember, this is a poc. For the moment, the "table" is a string with a json structure, that contain some information about the mode of extraction,url,options, etc. 

### example

```
for the query:

    select * from 'select * from '{"parser":"web-table","url":\"http://www.example.com/customers.html"}' where id = 'customers'

the output should by:

    id          | table_id      |   c1    |   c2    |   c3
    customers   | 1             | Company | Contact | Country
    customers   | 1             | KyC ASC | Juan A  | Chile
    ...
    
```
### sql parser

the sql parser is a fork of the project "mozilla:moz-sql-parser" with a some minimal changes (example, the table it is not a ident symbol, instead is a string for the moment). 

### python libraries


```
sudo pip install -U pyparsing
sudo pip install -U mo_future
sudo pip install -U lxml
```
