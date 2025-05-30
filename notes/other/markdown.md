# How to write markdown

Simple guide to use the basic markdown commands.
The official documentation is [here](https://daringfireball.net/projects/markdown/).

### Basic commands

Section headers are formatted using from 1 to 6 # (hash) character at the beginnign of the line.
For example, the above header has been obtained by typing `### Basic commands`.

Block quotes are formatted in a similar manner to emails, using the `>` (angle bracket) sign.
> This is a quote.

Carriage return is achieved by a backslash `\` at the end of a line.
For example this line ends \
on a new line.

Emphasys on text is obtained by enclosing the text between `*`, `_`, `**` or `__`. Here are the examples:
* *italic*  `*italic*`
* _italic_  `_italic_`
* **bold**  `**bold**`
* __bold__  `__bold__`

To format some `code` enclose it between backtick quotes, i.e. `` `code` ``.

Similarly, code blocks can be obtained by enclosing text between triple backticks ` ``` `:
```python
import pollo
print('Hello Pollo!')
```
Some markdown processor have syntax highlightning, just specify the language after the triple backtick, e.g. ` ```python `.

List are formatted by simply start a newline with `*`, `-` or `+`. For example:
- some item `- some item`
- another `- another`
- something else `- something else`

For numbered lists use `1.`, `2.`, `etc` as below
1. First `1. First`
2. Second `2. Second`
3. Third `3. Third`

### Links and images

Links are created with 2 similar syntax.
- The *inline* syntax is simply `[my website](https://tentacolo.com)`. The latter produces, [my website](https://tentacolo.com).
- The *reference* syntax has two elements. The actual link is `[my website][teno]`.
And the url is defined later with `[teno]: https://tentacolo.com`

For example, [my website][teno], [again my website][teno], [the same][teno].

Images are created similarly to links via an `!` exlamation mark, e.g. `![pollo-picture](pollo.jpg)`.
The latter produces the following
![pollo-picture](pollo.jpg)

Finally, images can be used as link buttons. We combine the two syntax as `[![pollo](pollo.jpg)](https://tentacolo.com)`.
The latter command produces the following link image:

[![pollo](pollo.jpg)](https://tentacolo.com)

### Vscode extensions

Finally, a short paragraph about the vscode extensions that I use for writing markdown.
There are many extension to improve the writing of markdown files
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
- [markdown all in one](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)

Further setting that I use just for markdown projects.  
Go to `file`->`preferences`->`settings` and type `@lang:markdown`. Then select:
- editor.wordBasedSuggestions: off. 
- editor.quickSuggestions: other: on.

This way I don't get **plain text** suggestion but I do get **code snippet** suggestion while typing. Nice!

At last, I don't like many of the default intellisense snippets. To avoid them to pop up while type do the following:
- `ctrl`+`shift`+`P` to open the control palette
- type `insert snippets` to open the list of available snippets
- with the mouse, click on the eye icon to hide the snippet

[teno]: https://tentacolo.com
