'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    letter = letter.upper()
    index = alphabet.find(letter)
    move = (alphabet.find(letter) + shift) % 26

    str = alphabet[move]

def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    message = message.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(message)
    str = ""
    for index in range(0, length):
        if message[index] == " ":
            converted_letter = " "
            str += converted_letter
        else:
            converted_letter = alphabet[(alphabet.find((message[index]))+shift)%26]
            str += converted_letter
    
    return str
    
    

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter = letter.upper()
    letter_shift = letter_shift.upper()
    pos1 = alphabet.find(letter)
    pos2 = (alphabet.find(letter_shift))+1
    
    if letter == " ":
        return " "

    str = alphabet[(pos1+pos2)%26]
    return str

def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    key = key.upper()
    length_message = len(message)
    length_key = len(key)
    
    if ' ' in key:
        return "Input a key with no spaces."
    
    if length_message > length_key:
        key = int((length_message/length_key)+1)*key
        new_key = ""
        for letter in range(0,length_message):
            new_key += key[letter]

    else:
        new_key = ""
        for letter in range(0,length_message):
            new_key += key[letter]

    pos1 = alphabet.find(message)
    str=""
    
    for index in range(0, length_message):
        if message[index] == " ":
            converted_letter = " "
            str += converted_letter
        else:
            shift = alphabet.find(new_key[index])+1
            converted_letter = alphabet[(alphabet.find(message[index])+shift)%26]
            str += converted_letter
            
    return str

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    message = message.upper()
    length = len(message)
    
    if len(message) % shift != 0:
        for extra in range(0,shift-(length%shift)):
            message += "_"
            length = len(message)

    str = ""
    
    for i in range(0,length):
        str += message[(i // shift) + (len(message) // shift) * (i % shift)]
    
    return str

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    message = message.upper()
    length = len(message)
    
    new_str = ""
    column = int(length/shift)
    start = 0
    
    while start <= shift-1:
        for index in range(0,column):
            new_str += message[index*shift+start]
        
        start += 1
    
    str = ""
    
    for letter in range(0,length):
        if new_str[letter] == "_":
            str += " "
        else:
            str += new_str[letter]
        
    #to remove excess space
    counter = 1       
    while str[len(str)-counter] == " ":
        str = str[0:len(str)-counter]
        counter += 1
    
    return str