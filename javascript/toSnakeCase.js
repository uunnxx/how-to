const toSnakeCase = str =>
  str &&
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map(x => x.toLowerCase())
    .join('_');


console.log(toSnakeCase('camelCase'));
console.log(toSnakeCase('some text'));
console.log(toSnakeCase('some-mixed_string With spaces_underscores-and-hyphens'));
console.log(toSnakeCase('AllThe-small Things'));
console.log(toSnakeCase('IAmListeningToFMWhileLoadingDifferentURLOnMyBrowserAndAlsoEditingSomeXMLAndHTML'));
