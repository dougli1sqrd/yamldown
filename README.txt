# Yamldown

This library allows users to load and read "YAMLdown" files. That is,
Markdown (primarily for github) with YAML embedded inside. Github markdown
already renders YAML style text in markdown as a table. This library parses
a yamldown file into its respective YAML and markdown.

## Installation

`pip install yamldown`

## Usage

Importing the yamldown module will let you `load` and `dump` yamldown files.
`load` receives a file-like object (backed by text in yamldown format) and
returns a tuple, first a dictionary with the containing YAML, and second a
string with the contents of the Markdown. In this way the yaml can be utilized.

Example:

    $ python3
    >>> import io
    >>> import yamldown
    >>>s = """
    ...---
    ...things:
    ...  - hello
    ...  - world
    ...foo: bar
    ...---
    ...This is some markdown text"""
    >>>f = io.StringIO(s)
    >>>yml, md = yamldown.load(f)
    >>>print(yml)
    {'things': ['hello', 'world'], 'foo': 'bar'}
    >>>print(md)
    This is some markdown text

To write out a yamldown file, `dump` takes a dictionary with your yaml data
and a string of markdown and outputs a string. The order in which the yaml
appears in the document can be specified with the `yamlfirst` option: `True`
for if the yaml should appear first (like in the above example) and `False` to
appear last.

Example:

    $ python3
    >>> import yamldown
    >>> yml = {'things': ['hello', 'world'], 'foo': 'bar'}
    >>> md = "This is some markdown text"
    >>> print(yamldown.dump(yml, md))
    ---
    foo: bar
    things:
    - hello
    - world

    ---
    This is some markdown text
