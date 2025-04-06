## Format String


### Custom fstring commands

```python

class Text:
    def __init__(self, text: str) -> None:
        self.text = text

    def __format__(self, format_spec: str) -> str:
        match format_spec:
            case 'upper':
                return self.text.upper()
            case 'lower':
                return self.text.lower()
            case 'len':
                return self.text.__len__().__str__()
            case _:
                raise Exception('Unknown format')




text: Text = Text('Hello, world!')

print(f"{text:len}")
print(f"{text:upper}")
print(f"{text:lower}")

```


### Chain of formatters

```python

class FormattedText:
    def __init__(self, text: str) -> None:
        self.text: str = text

    @override
    def __format__(self, format_spec: str):
        if format_spec and ':' in format_spec:
            parts: list[str] = format_spec.split(':')
            for part in parts:
                match part:
                    case "upper":
                        self.text = self.text.upper()
                    case "reverse":
                        components = self.text.split()
                        self.text = self.text.reverse() # logic for reversing
                    case "lower":
                        self.text = self.text.lower()
                    case "title":
                        self.text = self.text.title()
                    case _:
                        pass

        return self.text


text2: FormattedText = FormattedText('Hello, world!')

print(f"{text2:lower:reverse}")
print(f"{text2:title:reverse}")

```
