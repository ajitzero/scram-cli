import click

# Supported functions
CHOICES = [
    'caeser',
    'reverse'
]

# Driver function
@click.command()
@click.option('--hash-type', type=click.Choice(CHOICES), help="Encoding algorithm")
def cli(hash_type):
    """scram encodes the entered string depending on chosen hash-type. Ignores non-alphabets."""

    if hash_type is None:

        # Show menu
        click.echo("Select [--hash-type] option: " + ", ".join(CHOICES))

    else:

        # Take input
        ORIGINAL_MSG = click.prompt("Enter your message to be encoded", type=str).strip()

        # Apply handler function
        ENCODED_MSG = encoder(ORIGINAL_MSG, hash_type)
        
        # Display encoded message
        display(ENCODED_MSG)
        
def display(msg):
    """Displays the result"""

    click.echo()
    click.echo("Output: " + msg)
    click.echo()

def encoder(msg, hash_type):
    """Returns encoded message"""

    # Convert message to list
    result = [elem for elem in msg]

    if hash_type == 'caeser':
        """Implement Caeser Cipher Algorithm with offset"""

        # Input cipher offset
        offset = click.prompt("Enter offset", type=int)

        # Preserving offset sign before applying modulus
        offset_sign = '-' if offset < 0 else '+'

        # Removing excess offset
        offset = abs(offset) % 26
        if offset_sign == '-':
            offset *= (-1)

        # Storing ASCII values for range limits
        v_a = ord('a')
        v_A = ord('A')
        v_z = ord('z')
        v_Z = ord('Z')

        for i in range(len(result)):

            # Storing ASCII value for current element
            res_i = ord(result[i])

            # Check if within range [a to z, A to z]
            if v_A <= res_i <= v_Z or v_a <= res_i <= v_z:
                ul_case = True # Uppercase
                if v_a <= res_i <= v_z:
                    ul_case = False # Lowercase
                res_i += offset

                # On update, check if still within range [a to z, A to z]
                if v_A <= res_i <= v_Z or v_a <= res_i <= v_z:
                    result[i] = chr(res_i)

                elif ul_case:

                    # Uppercase
                    if res_i < v_A:
                        result[i] = chr(res_i + 25)
                    else:
                        result[i] = chr(res_i - 26)

                else:

                    # Lowercase
                    if res_i < v_a:
                        result[i] = chr(res_i + 26)
                    else:
                        result[i] = chr(res_i - 26)

        return ''.join(result)

    elif hash_type == 'reverse':
        """Apply Simple Reversal Algorithm"""

        return ''.join(reversed(result))

    else:
        click.echo("Error: Unsupported option.")
        pass
