# MasterPackage

> Auto-generated documentation for [mypy_boto3_builder.structures.master_package](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/master_package.py) module.

Structure for mypy-boto3 module.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / MasterPackage
    - [MasterPackage](#masterpackage)
        - [MasterPackage().essential_service_names](#masterpackageessential_service_names)

## MasterPackage

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/master_package.py#L12)

```python
class MasterPackage(Package):
    def __init__(
        name: str = LEGACY_MODULE_NAME,
        pypi_name: str = LEGACY_PYPI_NAME,
        service_names: Iterable[ServiceName] = tuple(),
        service_packages: Iterable[ServicePackage] = tuple(),
    ):
```

Structure for mypy-boto3 package.

#### See also

- [LEGACY_MODULE_NAME](../constants.md#legacy_module_name)
- [LEGACY_PYPI_NAME](../constants.md#legacy_pypi_name)
- [Package](package.md#package)

### MasterPackage().essential_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/master_package.py#L28)

```python
@property
def essential_service_names() -> List[ServiceName]:
```
