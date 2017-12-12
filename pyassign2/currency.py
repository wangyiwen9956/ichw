#!/usr/bin/env python3

"""Foobar.py: Description of what foobar does.

__author__ = "WangYiwen"
__pkuid__  = "1700011805"
__email__  = "wangyiwen@pku.edu.cn"
"""

from urllib.request import urlopen

def before_space(s):
    """Returns: Substring of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    index_of_space=s.index(" ")
    return s[0:index_of_space]


def after_space(s):
    """Returns: Substring of s after the first space

    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    index_of_space=s.index(" ")
    return s[index_of_space+1:]


def first_inside_quotes(s):
    """Returns: The first substring of s between two (double) quote 
    characters
    
    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote 
    characters inside."""
    first_quote=s.index('"')
    second_quote=s.index('"',first_quote+1)
    return s[first_quote+1:second_quote]


def get_from(json):
    """Returns: The FROM value in the response to a currency query.
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    index_of_colon=json.find(':')
    json=json[index_of_colon:]
    return first_inside_quotes(json)


def get_to(json):
    """Returns: The TO value in the response to a currency query.
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    index_of_colon=json.find(':')
    json=json[index_of_colon+1:]
    index_of_colon=json.find(':')
    json=json[index_of_colon+1:]
    return first_inside_quotes(json)


def has_error(json):
    """Returns: True if the query has an error; False otherwise.
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    if json.find('false')==-1:
        return False
    else:
        return True


def currency_response(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query.
    
    A currency query converts amount_from money in currency currency_from 
    to the currency currency_to. The response should be a string of the form
    
        '{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'
    
    where the values old-amount and new-amount contain the value and name 
    for the original and new currencies. If the query is invalid, both 
    old-amount and new-amount will be empty, while "success" will be followed 
    by the value false.
    
    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={}&to={}&amt={:f}'.format(currency_from,currency_to,amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a string."""
    return not has_error(currency_response(currency,'USD',1.0))

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    if iscurrency(currency_from) and iscurrency(currency_to):
        jstr=currency_response(currency_from,currency_to,amount_from)
        return float(before_space(get_to(jstr)))
    else:
        print("error")


def testA():
    """This function tests several cases of before_space(s) and 
    after_space(s)."""
    assert before_space("ab cde")=="ab"
    assert before_space("ab cde fg")=="ab"
    assert before_space(" ab cde")==""

    assert after_space("ab cde")=="cde"
    assert after_space("ab cde fg")=="cde fg"
    assert after_space(" ab cde")=="ab cde"


def testB():
    """This function tests several cases of first_inside_quotes(s),
    get_from(json), get_to(json) and has_error(json)""" 
    assert first_inside_quotes('a"bc"de')=="bc"
    assert first_inside_quotes('a"bc"de"f"g')=="bc"
    assert first_inside_quotes('"a"bc"de"f"g')=="a"
    assert first_inside_quotes('abcd""')==""
    json1= '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'
    assert get_from(json1)=='2 United States Dollars'
    assert get_to(json1)=='1.825936 Euros'
    assert has_error(json1)==False
    json2='{"from":"","to":"","success":false,"error":"Source currency code is invalid."}'
    assert get_from(json2)==''
    assert get_to(json2)==''
    assert has_error(json2)==True


def testC():
    """This function tests several cases of 
    currency_response(currency_from,currency_to,amount_from)."""
    assert currency_response('USD','EUR',2.5)=='{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'
    assert currency_response('AAA','EUR',2.5)=='{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'
    assert currency_response('USD','AAA',2.5)=='{ "from" : "", "to" : "", "success" : false, "error" : "Exchange currency code is invalid." }'


def testD():
    """This function tests several cases of is_currency(currency)
    and exchange(currency_from,currency_to,amount_from)."""
    assert iscurrency('USD')==True
    assert iscurrency('KES')==True
    assert iscurrency('kes')==False
    assert iscurrency('aaa')==False
    assert exchange('USD','EUR',2.5)-2.0952375<=0.000001
    assert exchange('USD','KES',5.4)-557.4752586<=0.000001
    assert exchange('LKR','NGN',1.7)-3.9997994984588<=0.000001


def test_all():
    """This function tests several cases of is_currency(currency)
    and exchange(currency_from,currency_to,amount_from)."""
    testA()
    testB()
    testC()
    testD()
    print('all tests passed')

    
def main():
    """This function call testA,testB,testC and testD."""
    currency_from=input()
    currency_to=input()
    amount_from=float(input())
    print(exchange(currency_from,currency_to,amount_from))
    test_all()

    
if __name__ == "__main__":
    main()
