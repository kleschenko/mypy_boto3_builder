# Strings

> Auto-generated documentation for [mypy_boto3_builder.utils.strings](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/utils/strings.py) module.

Multiple string utils collection.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](index.md#utils) / Strings
    - [get_anchor_link](#get_anchor_link)
    - [get_class_prefix](#get_class_prefix)
    - [get_line_with_indented](#get_line_with_indented)
    - [is_reserved](#is_reserved)

## get_anchor_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/utils/strings.py#L91)

```python
def get_anchor_link(text: str) -> str:
```

Convert header to markdown anchor link.

## get_class_prefix

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/utils/strings.py#L18)

```python
def get_class_prefix(func_name: str) -> str:
```

Get a valid Python class prefix from `func_name`.

#### Arguments

- `func_name` - Any string.

#### Returns

String with a class prefix.

## get_line_with_indented

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/utils/strings.py#L32)

```python
def get_line_with_indented(
    input_string: str,
    multi_first_line: bool = False,
) -> str:
```

Get first line of the string with all indented lines.

Fixes invalid unindent.

#### Arguments

- `input_string` - Input string.

#### Returns

A string with first line and following indented lines.

## is_reserved

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/utils/strings.py#L98)

```python
def is_reserved(word: str) -> bool:
```

Check whether varialbe name conflicts with Python reserved names.
