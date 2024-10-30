# Example project to demonstrate issue with the width (line-length) parameter

TLDR; when the library is configured using `yaml.width = 80`, the generated file can  have lines length that exceeds 80 characters.
Bug reported here: https://sourceforge.net/p/ruamel-yaml/tickets/529/

ruamel version: `0.18.6`


## Setup the project
`pipenv install`

## Run the test
`pipenv run python -m unittest discover`

Test output:
```bash
AssertionError: 84 not less than or equal to 80 : Line exceeds 80 characters:         key: this is a quite long string that should be reformatted to use less than (Length: 84)

```

