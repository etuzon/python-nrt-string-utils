import pytest

from nrt_string_utils.string_utils import StringUtil
from tests.string_utils_data import sub_string_list_data, sub_string_data, json_data, \
    char_and_ascii_number_pairs_data, emails_data, urls_data


def test_decode_base64():
    assert StringUtil.decode_base64('dGVzdA==') == 'test'
    assert StringUtil.decode_base64('dGVzdA==') != 'test1'


def test_encode_base64():
    assert StringUtil.encode_base64('test') == 'dGVzdA=='
    assert StringUtil.encode_base64('test') != 'dGVzdA==1'


@pytest.mark.parametrize(
    'text, expected_char_and_ascii_number_pairs', char_and_ascii_number_pairs_data)
def test_get_char_and_ascii_number_pairs(text, expected_char_and_ascii_number_pairs):
    assert StringUtil.get_char_and_ascii_number_pairs(text) \
           == expected_char_and_ascii_number_pairs


@pytest.mark.parametrize('text, expected_emails', emails_data)
def test_get_emails(text, expected_emails):
    assert __compare_lists(StringUtil.get_emails(text), expected_emails)


def test_get_last_char():
    assert StringUtil.get_last_char('test') == 't'
    assert StringUtil.get_last_char('') == ''
    assert StringUtil.get_last_char(' ') == ' '
    assert StringUtil.get_last_char('1') == '1'
    assert StringUtil.get_last_char('1.0') == '0'
    assert StringUtil.get_last_char('1.0 ') == ' '
    assert StringUtil.get_last_char('1.0 \nav') == 'v'
    assert StringUtil.get_last_char('1.0 d\n') == '\n'


@pytest.mark.parametrize('text, expected_urls', urls_data)
def test_get_urls(text, expected_urls):
    assert __compare_lists(StringUtil.get_urls(text), expected_urls)


def test_is_decimal():
    assert StringUtil.is_decimal('0')
    assert StringUtil.is_decimal('-1')
    assert StringUtil.is_decimal('1')
    assert StringUtil.is_decimal('1.0')
    assert not StringUtil.is_decimal('1.0 ')
    assert not StringUtil.is_decimal(' 1.0')
    assert not StringUtil.is_decimal('1.2 \n')
    assert not StringUtil.is_decimal('1.4 \na')
    assert not StringUtil.is_decimal('1.0.0')
    assert not StringUtil.is_decimal('1.0.')
    assert not StringUtil.is_decimal('')
    assert not StringUtil.is_decimal(None)


def test_is_int():
    assert StringUtil.is_int('0')
    assert StringUtil.is_int('-1')
    assert StringUtil.is_int('1')
    assert not StringUtil.is_int('1.0')
    assert not StringUtil.is_int('1.0 ')
    assert not StringUtil.is_int(' 1.0')
    assert not StringUtil.is_int('1.5 \n')
    assert not StringUtil.is_int('1.6 \na')
    assert not StringUtil.is_int('1.0.0')
    assert not StringUtil.is_int('')
    assert not StringUtil.is_int(None)


@pytest.mark.parametrize('text, expected', json_data)
def test_is_json(text, expected):
    assert StringUtil.is_json(text) == expected


def test_is_positive_decimal():
    assert StringUtil.is_positive_decimal('1')
    assert StringUtil.is_positive_decimal('1.0')
    assert not StringUtil.is_positive_decimal('0')
    assert not StringUtil.is_positive_decimal('-1')
    assert not StringUtil.is_positive_decimal('1.0 ')
    assert not StringUtil.is_positive_decimal(' 1.0')
    assert not StringUtil.is_positive_decimal('1.7 \n')
    assert not StringUtil.is_positive_decimal('1.8 \na')
    assert not StringUtil.is_positive_decimal(None)


def test_is_positive_int():
    assert StringUtil.is_positive_int('1')
    assert not StringUtil.is_positive_int('0')
    assert not StringUtil.is_positive_int('-1')
    assert not StringUtil.is_positive_int('1.0')
    assert not StringUtil.is_positive_int('1.0 ')
    assert not StringUtil.is_positive_int(' 1.0')
    assert not StringUtil.is_positive_int('1.9 \n')
    assert not StringUtil.is_positive_int('1.11 \na')
    assert not StringUtil.is_positive_int(None)


def test_is_unsigned_decimal():
    assert StringUtil.is_unsigned_decimal('1')
    assert StringUtil.is_unsigned_decimal('1.0')
    assert StringUtil.is_unsigned_decimal('0')
    assert not StringUtil.is_unsigned_decimal('-1')
    assert not StringUtil.is_unsigned_decimal('1.0 ')
    assert not StringUtil.is_unsigned_decimal(' 1.0')
    assert not StringUtil.is_unsigned_decimal('1.0 \n')
    assert not StringUtil.is_unsigned_decimal('1.0 \na')
    assert not StringUtil.is_unsigned_decimal(None)


def test_is_unsigned_int():
    assert StringUtil.is_unsigned_int('1')
    assert StringUtil.is_unsigned_int('0')
    assert not StringUtil.is_unsigned_int('-1')
    assert not StringUtil.is_unsigned_int('1.0')
    assert not StringUtil.is_unsigned_int('1.0 ')
    assert not StringUtil.is_unsigned_int(' 1.0')
    assert not StringUtil.is_unsigned_int('1.0 \n')
    assert not StringUtil.is_unsigned_int('1.0 \na')
    assert not StringUtil.is_unsigned_int('0.0')
    assert not StringUtil.is_unsigned_int(None)


@pytest.mark.parametrize(
    'text, start_delimiter, end_delimiter, expected_sub_string', sub_string_data)
def test_sub_string(text, start_delimiter, end_delimiter, expected_sub_string):

    sub_string = StringUtil.sub_string(text, start_delimiter, end_delimiter)
    assert sub_string == expected_sub_string


@pytest.mark.parametrize(
    'text, start_delimiter, end_delimiter, expected_sub_string_list',
    sub_string_list_data)
def test_sub_string_list(
        text, start_delimiter, end_delimiter, expected_sub_string_list):

    sub_string_list = StringUtil.sub_string_list(text, start_delimiter, end_delimiter)
    assert sub_string_list == expected_sub_string_list


def test_to_ascii():
    assert StringUtil.to_ascii('test') == 'test'
    assert StringUtil.to_ascii('test ') == 'test '
    assert StringUtil.to_ascii('') == ''
    assert StringUtil.to_ascii('testこんにちは123') == 'test123'


def __compare_lists(list_1, list_2):
    if len(list_1) != len(list_2):
        return False

    for item in list_1:
        if item not in list_2:
            return False

    for item in list_2:
        if item not in list_1:
            return False

    return True
