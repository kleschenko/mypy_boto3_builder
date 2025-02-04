# Paginator

> Auto-generated documentation for [mypy_boto3_builder.structures.paginator](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/paginator.py) module.

Boto3 client Paginator.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Paginator
    - [Paginator](#paginator)
        - [Paginator().boto3_doc_link](#paginatorboto3_doc_link)
        - [Paginator().docstring](#paginatordocstring)
        - [Paginator().get_client_method](#paginatorget_client_method)

## Paginator

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/paginator.py#L18)

```python
class Paginator(ClassRecord):
    def __init__(
        name: str,
        paginator_name: str,
        operation_name: str,
        service_name: ServiceName,
    ):
```

Boto3 client Paginator.

#### See also

- [ClassRecord](class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### Paginator().boto3_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/paginator.py#L38)

```python
@property
def boto3_doc_link() -> str:
```

### Paginator().docstring

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/paginator.py#L42)

```python
@property
def docstring() -> str:
```

### Paginator().get_client_method

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/paginator.py#L51)

```python
def get_client_method() -> Method:
```

#### See also

- [Method](method.md#method)
