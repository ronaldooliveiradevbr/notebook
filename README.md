# Notebook CLI

A simple object-oriented notebook implementation, written in Python, primarily focused on running in terminal.


## Requirements

* Python: 3.6+



## How to run it

1. Clone this repo and get into it:
```console
$ git clone https://github.com/rfdeoliveira/notebook.git
$ cd notebook
```

2. Create and activate a virtual environment:
```console
$ python -m venv .notebook
$ source .notebook/bin/activate
```

3. Run unit tests
```console
$ python -m unittest
```

4. Open a python interpreter, import notebook module and play with it =):
```console
$ python
>>> from notebook import Note
>>>
>>>
>>> new_note = Note('my memo', tags='first_note testing') # instantiating a new note
>>>
>>>
>>> new_note.match('memo') # matching a note against a queries
True
>>> new_note.match('second note')
False
```


## TO-DO

* [x] A Note Class

* [ ] A Notebook Class

* [ ] A CLI Menu

* [ ] CI badge

* [ ] Test coverage badge

* [ ] Code quality badge
