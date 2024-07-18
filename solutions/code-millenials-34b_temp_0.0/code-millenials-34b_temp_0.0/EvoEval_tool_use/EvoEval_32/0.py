def is_starting_char(ch: str) -> bool:
  """
  Checks whether given character is a valid starting character for a variable name in our language.
  Our language allows a variable to start with an underscore or a letter.
  """
  if ch.isalpha() or ch == '_':
    return True
  return False

def is_valid_char(ch: str) -> bool:
  """
  Checks whether given character is a valid character for a variable name in our language.
  Our language allows a variable to contain underscores, letters and digits.
  """
  if ch.isalpha() or ch == '_' or ch.isdigit():
    return True
  return False
def validate_identifier(identifier: str) -> bool:
    """
  In our programming language, an identifier is valid if it starts with a letter or an underscore,
  and the rest of the identifier can contain any combination of letters, digits, and underscores.

  This function should return True if given string is a valid identifier in our language, and False otherwise.

  >>> validate_identifier("_valid_variable")
  True
  >>> validate_identifier("2_invalid_variable")
  False
  """
    if len(identifier) == 0:
        return False
    if not is_starting_char(identifier[0]):
        return False
    for ch in identifier[1:]:
        if not is_valid_char(ch):
            return False
    return True