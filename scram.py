import click
import pyperclip
import encoder

# Supported functions
CHOICES = [
    'affine',
    'ascii',
    'atbash',
    'binary',
    'caeser',
    'morse',
    'none',
    'polybius-square',
    'reverse',
    'reverse-words',
    'vignere'
]

# Driver function
@click.command()
@click.option('--hash-type', '-h', multiple=True, type=click.Choice(CHOICES), help="Choose algorithm.")
@click.option('--version', '-v', multiple=True, is_flag=True, help="Show current version.")
def cli(version, hash_type):
    """scram encodes/encrypts the entered string depending on the chosen algorithm. Ignores non-alphabets."""

    if len(version) > 0 and version[0]:
        click.echo("Scram CLI v.1.0")

    else:
        if hash_type is None or not len(hash_type):

            # Show menu
            click.echo("Select [-h, --hash-type] option: " + ", ".join(CHOICES))

        else:
            
            # In case [-h] is used of [--hash-type]
            if isinstance(hash_type, tuple):
                hash_type = hash_type[0]

            # Take input
            ORIGINAL_MSG = click.prompt("Enter your message to be encoded", type=str).strip()

            # Apply handler function
            ENCODED_MSG = encoder.calc(ORIGINAL_MSG, hash_type)

            # Display encoded message
            display(ENCODED_MSG)

# Components
def display(MSG):
    """Displays the result"""

    click.echo("Output: " + MSG)

    # Copy to clipboard
    if click.prompt("Copy result to clipboard? [y|n]", type=str).strip().lower() in "yes":
        pyperclip.copy(MSG)
        click.echo("Copied to clipboard successfully.")
    else:
        click.echo("Command terminated normally.")
