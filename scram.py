import click
import encoder

# Supported functions
CHOICES = [
    'caeser',
    'reverse'
]

# Driver function
@click.command()
@click.option('--hash-type', '-h', multiple=True, type=click.Choice(CHOICES), help="Choose algorithm.")
@click.option('--version', '-v', multiple=True, is_flag=True, help="Show current version.")
def cli(version, hash_type):
    """scram encodes/encrypts the entered string depending on the chosen algorithm. Ignores non-alphabets."""

    # print(type(hash_type), hash_type)
    if len(version) > 0 and version[0]:
        click.echo("Scram CLI v.0.1")

    else:
        if hash_type is None:

            # Show menu
            click.echo("Select [--hash-type] option: " + ", ".join(CHOICES))

        else:
            
            # In case [-h] is used of [--hash-type]
            if isinstance(hash_type, tuple):
                hash_type = hash_type[0]

            # Take input
            ORIGINAL_MSG = click.prompt("Enter your message to be encoded", type=str).strip()

            # Apply handler function
            ENCODED_MSG = encoder.encoder(ORIGINAL_MSG, hash_type)

            # Display encoded message
            display(ENCODED_MSG)
            
def display(msg):
    """Displays the result"""

    click.echo("\n" + "Output: " + msg + "\n")
