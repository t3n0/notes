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
- [markdown preview enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)

The third one is especially useful because it also recognise the markdown environments of jupyter cells.
This means that when we are editing any jupyter markdown cell, we can set a side panel with the preview and see the markdown cell being rendered live! Very useful!

To convert `.md` files to `.pdf`, I follow either of the following two methods:
1. right click **in the document** and select convert to `html`; then open the browser and select export to `pdf` from the file dropdown menu, or
2. right click **in the preview** and select `export`->`chrome-puppeteer`->`pdf`.

The second method requires:
- installation of `chrome` ([here](https://www.google.com/chrome/))
- set the path to `chrome`: from `settings` set the option `markdown-preview-enhanced.chromePath` to `/usr/bin/google-chrome`

Many people on the internet suggest to use tools such as `nbconverter`, `pandoc`, `markdown-pdf` extension, and the like.
Honestly, I tried all of them and there are always problems when rendering the math.
The two approaches descibed above is the ones that produce good math formulas and do not require too much tinkering with libraries and stuff.

Further setting that I use just for markdown projects.  
Go to `file`->`preferences`->`settings` and type `@lang:markdown`. Then select:
- editor.wordBasedSuggestions: off. 
- editor.quickSuggestions: other: on.

This way I don't get **plain text** suggestion but I do get **code snippet** suggestion while typing. Nice!

At last, I don't like many of the default intellisense snippets. To avoid them to pop up while type do the following:
- `ctrl`+`shift`+`P` to open the control palette
- type `insert snippets` to open the list of available snippets
- with the mouse, click on the eye icon to hide the snippet

#### Some useful snippets

Navigate to `File`->`Preferences`->`Configure snippets` and select `markdown` from the control palette.
This will open the `markdown.json` file. Edit it by adding your favorite snippets.

Equation environment within dollar signs
  ```
  "latex equation": {
		"prefix": "equation",
		"body": [
			"$$\n\\begin{equation}\n\t${1:x = y}\n\\end{equation}\n$$",
		],
		"description": "Latex equation environment"
	},
  ```

[teno]: https://tentacolo.com
