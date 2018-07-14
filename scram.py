import click
import encoder

# Supported functions
CHOICES = [
    'caeser',
    'reverse'
]

# Driver function
@click.command()
@click.option('--hash-type', type=click.Choice(CHOICES), help="Choose algorithm.")
def cli(hash_type):
    """scram encodes/encrypts the entered string depending on chosen hash-type. Ignores non-alphabets."""

    if hash_type is None:

        # Show menu
        click.echo("Select [--hash-type] option: " + ", ".join(CHOICES))

    else:

        # Take input
        ORIGINAL_MSG = click.prompt("Enter your message to be encoded", type=str).strip()

        # Apply handler function
        ENCODED_MSG = encoder.encoder(ORIGINAL_MSG, hash_type)
        
        # Display encoded message
        display(ENCODED_MSG)
        
def display(msg):
    """Displays the result"""

    click.echo()
    click.echo("Output: " + msg)
    click.echo()
