import sys
from types import ModuleType


class VerboseModule(ModuleType):
    def __repr__(self) -> str:
        return f'Verbose {self.__name__}'

    def __setattr__(self, attr: str, value: str) -> None:
        print(f'Setting {attr}...')
        super().__setattr__(attr, value)


sys.modules[__name__].__class__ = VerboseModule
