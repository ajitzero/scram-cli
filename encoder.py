import click
import string

def calc(MSG, hash_type):
    """Returns encoded message"""

    # Preprocess message to list
    result = [elem for elem in MSG]

    if hash_type == 'affine':
        """Apply Affine Cipher Algorithm"""

        # Input cipher offset
        key1 = click.prompt("Enter key 1", type=int)
        key2 = click.prompt("Enter key 2", type=int)

        result = ''
        for elem in MSG:
            if elem == ' ':
                result += elem
            else:
                result += chr((((key1 * (ord(elem) - ord('A'))) + key2) % 26) + ord('A'))
                
        return result

    elif hash_type == 'ascii':
        """Convert every character to ASCII representation"""
        
        result = [str(ord(elem)) for elem in MSG]
        return ' '.join(result)

    elif hash_type == 'atbash':
        """Apply Atbash Cipher Algorithm"""

        domain = string.ascii_lowercase[::-1]

        result = ''
        for elem in MSG.upper():
            if elem == ' ':
                result += elem
            else:
                result += domain[ord(elem) - 65]

        return result
        
    elif hash_type == 'binary':
        """Convert every character to binary representation"""

        result = [str(bin(ord(elem))[2:]) for elem in MSG]
        return ' '.join(result)
    
    elif hash_type == 'book':
        """Convert message to key representation"""
        
        passage = click.prompt("Enter passage", type=str)
        w_l=passage.split(' ')
        key=[]
        f_l_l=[a[0].lower() for a in w_l]
        for i in MSG.lower():
            if i not in f_l_l:
                raise ValueError("Error: The entered passage does not support the message.")
            if i in f_l_l:
                key.append(str(f_l_l.index(i)+1))
        return ','.join(key)
                
    elif hash_type == 'caeser':
        """Implement Caeser Cipher Algorithm with offset"""

        # Input cipher offset
        offset = click.prompt("Enter offset", type=int)

        # Preserving offset sign before applying modulus
        offset_sign = '-' if offset < 0 else '+'

        # Removing excess offset
        offset = abs(offset) % 26
        if offset_sign == '-':
            offset *= (-1)

        # Caching ASCII values for range limits
        v_a, v_A, v_z, v_Z = ord('a'), ord('A'), ord('z'), ord('Z')

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
            else:
                pass

        return ''.join(result)

    elif hash_type == 'morse':
        """Apply Substitution for morse code Algorithm"""

        # Store morse code values
        MORSE = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', ' ':'/' }

        result_new = []
        for elem in result:

            # Convert to uppercase
            new_elem = elem.upper()
            if new_elem in MORSE:
                result_new.append(MORSE[new_elem])
            else:
                raise ValueError("Error: " + str(elem) + " not supported in morse code.")

        return ' '.join(result_new)

    elif hash_type == 'polybius-square':
        """Apply Polybius Square Cipher Algorithm"""

        result = ""
        for elem in MSG.upper():

            row = (ord(elem) - ord('A')) // 5 + 1
            col = (ord(elem) - ord('A')) % 5 + 1

            if elem == 'K':
                row -= 1
                col = 6 - col

            elif ord(elem) >= ord('J'):
                if col == 1:
                    row -= 1
                    col = 6 
                col -= 1
            result += str(row) + str(col)

        return ''.join(result)

    elif hash_type == 'reverse':
        """Apply Simple Reversal Algorithm"""

        return ''.join(result[::-1])

    elif hash_type == 'reverse-words':
        """Reverse only words, in-place"""

        result = [str(''.join(elem[::-1])) for elem in ''.join(result).split()]
        return ' '.join(result)

    elif hash_type == 'vignere':
        """Reverse only words, in-place"""

        # Input cipher key
        key = click.prompt("Enter key", type=str).lower()
        key = ''.join(key.strip().split())

        result_new = ""
        domain = string.ascii_lowercase
        positions = [domain.find(elem) for elem in key]
        lenp = len(positions)

        status = 0
        for elem in MSG:
            if elem == " ":
                result_new += elem

            else:
                if status >= lenp:
                    status = 0
                current_pos = positions[status] + domain.find(elem)

                if current_pos > 25:
                  current_pos -= 26

                result_new += domain[current_pos]
                status += 1

        return ''.join(result_new)
    
     

    else:
        """Return original string"""

        return ''.join(result)

    
    
