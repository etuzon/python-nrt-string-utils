# String Utilities

### String utilities in Python.

![PyPI](https://img.shields.io/pypi/v/nrt-string-utils?color=blueviolet&style=plastic)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nrt-string-utils?color=greens&style=plastic)
![PyPI - License](https://img.shields.io/pypi/l/nrt-string-utils?color=blue&style=plastic)
![PyPI - Downloads](https://img.shields.io/pypi/dd/nrt-string-utils?style=plastic)
![PyPI - Downloads](https://img.shields.io/pypi/dm/nrt-string-utils?color=yellow&style=plastic)
[![Coverage Status](https://coveralls.io/repos/github/etuzon/python-nrt-string-utils/badge.svg)](https://coveralls.io/github/etuzon/pytohn-nrt-string-utils)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/etuzon/python-nrt-string-utils?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/etuzon/python-nrt-string-utils?style=plastic)
[![DeepSource](https://app.deepsource.com/gh/etuzon/python-nrt-string-utils.svg/?label=active+issues&show_trend=false&token=BiVHFqo8lcnkHT7oIOXLceZ3)](https://app.deepsource.com/gh/etuzon/python-nrt-string-utils/)

## StringUtil class

### Methods

| **Method**                        | **Description**                                                         | **Parameters**                                                                                                                                                              | **Returns**                                                                             |
|-----------------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| `decode_base64`                   | Decodes a base64 encoded string.                                        | `encoded_text (str)` The base64 encoded string to decode.                                                                                                                   | `str` The decoded string.                                                               |
| `encode_base64`                   | Encodes a string to base64.                                             | `text (str)` The string to encode.                                                                                                                                          | `str` The base64 encoded string.                                                        |
| `get_char_and_ascii_number_pairs` | Returns a list of tuples containing the character and its ASCII number. | `text (str)` The string to analyze.                                                                                                                                         | `list[tuple[str, int]]` A list of tuples containing the character and its ASCII number. |
| `get_emails`                      | Returns a list of email addresses found in a string.                    | `text (str)` The string to search for email addresses.                                                                                                                      | `list[str]` A list of email addresses found in the string (without duplications).       |
| `get_last_char`                   | Returns the last character of a string.                                 | `text (str)` The string to analyze.                                                                                                                                         | `str` The last character of the string.                                                 |
| `get_urls`                        | Returns a list of URLs found in a string.                               | `text (str)` The string to search for URLs.                                                                                                                                 | `list[str]` A list of URLs found in the string (without duplications).                  |
| `is_decimal`                      | Checks if a string is a decimal number.                                 | `text (Optional[str])` The string to check.                                                                                                                                 | `bool` True if the string is a decimal number, False otherwise.                         |
| `is_int`                          | Checks if a string is an integer.                                       | `text (Optional[str])` The string to check.                                                                                                                                 | `bool` True if the string is an integer, False otherwise.                               |
| `is_json`                         | Checks if a string is a valid JSON.                                     | `text (Optional[str])` The string to check.                                                                                                                                 | `bool` True if the string is a valid JSON, False otherwise.                             |
| `is_positive_decimal`             | Checks if a string is a positive decimal number.                        | `text (Optional[str])` The string to check.                                                                                                                                 | `bool` True if the string is a positive decimal number, False otherwise.                |
| `is_positive_int`                 | Checks if a string is a positive integer.                               | `text (Optional[str])` The string to check.                                                                                                                                 | `bool` True if the string is a positive integer, False otherwise.                       |
| `is_unsigned_decimal`             | Checks if a string is an unsigned decimal number.                       | `text (Optional[str])` The string to check.                                                                                                                                 | `bool` True if the string is an unsigned decimal number, False otherwise.               |
| `is_unsigned_int`                 | Checks if a string is an unsigned integer.                              | `text (Optional[str])` The string to check.                                                                                                                                 | `bool` True if the string is an unsigned integer, False otherwise.                      |
| `sub_string`                      | Returns a substring from a string.                                      | `text (str)` The string to extract the substring from.<br>`start_delimiter (str)` Sub string start delimiter.<br>`end_delimiter (Optional[str])` Sub string end delimiter.  | `str` The extracted substring.                                                          |
| `sub_string_list`                 | Returns a list of substrings from a string.                             | `text (str)` The string to extract the substrings from.<br>`start_delimiter (str)` Sub string start delimiter.<br>`end_delimiter (Optional[str])` Sub string end delimiter. | `list[str]` A list of extracted substrings.                                             |
| `to_ascii`                        | Converts a string to ASCII.                                             | `text (str)` The string to convert.                                                                                                                                         | `str` The ASCII representation of the string.                                           |

### Examples:

- #### StringUtil.decode_base64

    **Code**
    ```python
    from string_utils import StringUtil

    # Decode a base64 encoded string
    decoded_text = StringUtil.decode_base64('dGVzdA==')
    print(decoded_text)
    ```
    **Output**
    ```
    test
    ```

- #### StringUtil.encode_base64
    
    **Code**
    ```python
    from string_utils import StringUtil
    
    # Encode a string to base64
    encoded_text = StringUtil.encode_base64('test')
    print(encoded_text)
    ```
    **Output**
    ```
    dGVzdA==
    ```

- #### StringUtil.get_char_and_ascii_number_pairs

    **Code**
    ```python
    from string_utils import StringUtil
    
    # Get the character and its ASCII number pairs
    pairs = StringUtil.get_char_and_ascii_number_pairs('test')
    print(pairs)
    ```
    **Output**
    ```
    [('t', 116), ('e', 101), ('s', 115), ('t', 116)]
    ```
