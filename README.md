# Scram CLI

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

A command-line utility to encode messages, built with [Click](https://github.com/pallets/click) (Python 3).

> This project is created for learning about command-line application development and practicing the implementation of encoding algorithms. **This project is NOT meant for production and hasn't been tested thoroughly.**

## Installation

```sh

git clone git@github.com:AjitZero/Scram-CLI.git
cd Scram-CLI
pip install .

```

## Development Setup

Tested on `Ubuntu 18.04 LTS` and `Windows 10`.

```sh

git clone git@github.com:AjitZero/Scram-CLI.git
cd Scram-CLI
python3 -m venv env
source env/bin/activate
pip install --editable .

```

To exit the Virtual Environment, simply enter `deactivate`.

## Documentation

```

Usage: scram [OPTIONS]

  scram encodes/encrypts the entered string depending on the chosen
  algorithm. Ignores non-alphabets.

Options:
  -h, --hash-type [affine|ascii|atbash|binary|caeser|morse|none|polybius-square|reverse|reverse-words|vignere]
                                  Choose algorithm.
  -v, --version                   Show current version.
  --help                          Show this message and exit.

```

## Examples

```sh

$ scram -h caeser
Enter your message to be encoded: AjitZero
Enter offset: 5
Output: FonyEjwt
Copy result to clipboard? [y|n]: y
Copied to clipboard successfully.

$ scram -h morse
Enter your message to be encoded: Ajit Zero
Output: .- .--- .. - / --.. . .-. ---
Copy result to clipboard? [y|n]: n
Command terminated normally.

```

## Contributing

> All existing encoding algorithms require a corresponding **decoder** function. Have at it if you're interested!

1. [Fork](https://github.com/AjitZero/Scram-CLI/fork) it.
2. Create your feature branch. (`git checkout -b feature/yourfeature`)
3. Commit your changes. (`git commit -am 'Add some yourfeature'`)
4. Push to the branch. (`git push origin feature/yourfeature`)
5. Create a new Pull Request and link an [issue](https://github.com/AjitZero/Scram-CLI/issues/new) with it.

## Resources

| Topic | Reference | Link |
| --- | --- | --- |
| Affine cipher | Wikipedia | [Source](https://en.wikipedia.org/wiki/Affine_cipher) |
| ASCII code | Wikipedia | [Source](https://en.wikipedia.org/wiki/ASCII) |
| Atbash cipher | Wikipedia | [Source](https://en.wikipedia.org/wiki/Atbash_cipher) |
| Book cipher | Wikipedia | [Source](https://en.wikipedia.org/wiki/Book_cipher) |
| Caesar cipher | Wikipedia | [Source](https://en.wikipedia.org/wiki/Caesar_cipher) |
| Morse code | GeeksForGeeks | [Source](https://www.geeksforgeeks.org/morse-code-translator-python/) |
| Polybius Square | Wikipedia | [Source](https://en.wikipedia.org/wiki/Polybius_square) |
| Vigenère cipher | Wikipedia | [Source](https://en.wikipedia.org/wiki/Vigenère_cipher) |

## Meta

Ajit Panigrahi – [@AjitZero](https://github.com/AjitZero) – Ping me on [Twitter](https://twitter.com/AjitZero) or [Email me](mailto:ajitzero@gmail.com) for any queries.

Distributed under the [MIT License](https://opensource.org/licenses/MIT). See [`LICENSE`](https://github.com/AjitZero/Scram-CLI/blob/master/LICENSE) for more information.
