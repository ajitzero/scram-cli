# Scram CLI

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)

A command-line utility to encode & encrypt messages, built with [Click](https://github.com/pallets/click) (Python 3).
WIP.

## Development Setup

Only Linux supported for now (Tested on Ubuntu 18.04 LTS):

```sh
git clone git@github.com:AjitZero/Scram-CLI.git
cd Scram-CLI
python3 -m venv env
source env/bin/activate
pip install --editable .
```

To exit the Virtual Environment, simply enter `deactivate`.

## Usage example

```
Usage: scram [OPTIONS]

  scram encodes/encrypts the entered string depending on the chosen
  algorithm. Ignores non-alphabets.

Options:
  -h, --hash-type [caeser|reverse]
                                  Choose algorithm.
  -v, --version                   Show current version.
  --help                          Show this message and exit.

```


## TODO

- [ ] Add decoding/decryption functions.
- [ ] Refactor code into modules.
- [ ] Add copy to clipboard option.
- [ ] Add Windows support

## Contributing

1. [Fork](https://github.com/AjitZero/Scram-CLI/fork) it.
2. Create your feature branch. (`git checkout -b feature/yourfeature`)
3. Commit your changes. (`git commit -am 'Add some yourfeature'`)
4. Push to the branch. (`git push origin feature/yourfeature`)
5. Create a new Pull Request.

> Please [contact me](#meta) before submitting a Pull Request since I won't be accepting PRs without verifying its validity.

## Meta

Ajit Panigrahi – [@AjitZero](https://github.com/AjitZero) – Ping me on [Twitter](https://twitter.com/AjitZero) or [Email me](mailto:ajitzero@gmail.com) for any queries

Distributed under the MIT License. See `LICENSE` for more information.
