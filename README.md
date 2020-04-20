# Wordifier 
![wordify-test](https://github.com/shivaang12/wordifier/workflows/wordify-test/badge.svg)


A Python based vanity number generator. You can utilize the pacakge to generate possible vanity number upon providing a valid US phone number (Please see below for phone number compatibility).
Additionally, it can also take a vanity number and generate a valid all digit phone number. 


* Free software: MIT license


Features
--------

* Generates best possible vanity number from a valid US phone number.
* Generates all digit US phone number from a vanity number.
* Generates all possible combination of vanity number from a valid US phone number.


How do I use this
-----------------

After being in the project directory, please execute following command
```
pip install .
```
This will install `wordifier` for your python interpreter.
Then you can call `wordifier.wordifier.number_to_words("1-800-123-4567")` method which will spits out best possible
vanity number. For detail example, see below

```python
from wordifier import wordifier

print(wordifier.number_to_words("1-800-724-6837"))
```
output
```bash
"1-800-PAINTER"
```

The other two methods `wordifier.words_to_number` and `wordifier.all_wordification` can be accessed similarly.
For more information on these functions, you can type
```python
# For number_to_words method
help(wordifier.number_to_words)
# For words_to_number method
help(wordifier.words_to_number)
# For all_wordification method
help(wordifier.all_wordification)
```


For Developers
--------------

For development, I would recommend using virtual environment (cause it's more cleaner this way).
To install project dependencies, please use following command from the root of this project's directory

```
pip install -r requirements_dev.txt
```

This will also install the test dependent packages.

This project uses `tox` for testing.


TODO
----

* Support incomplete words
* Support return format such as `(XXX) XXX XXXX`, `XXX XXX XXXX` etc.
* Incorporate more tests for some corner cases.
* Solve TODOs inside the code.
* Generate Docs

Credits
-------

This package was created with Cookiecutter and the `audreyr/cookiecutter-pypackage` project template.

Cookiecutter: https://github.com/audreyr/cookiecutter

audreyr/cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
