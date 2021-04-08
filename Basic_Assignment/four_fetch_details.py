import re

def fetch_details(number):
    matcher = re.findall('[0-9]{1,4}', number)
    if len(matcher) == 4:
        number_dict = {
            'area-code': matcher[0],
            'phone-number': matcher[2],
            'extension': matcher[3],
            'trunk': matcher[1]
        }

    if len(matcher) == 3:
        number_dict = {
            'area-code': matcher[0],
            'phone-number': matcher[2],
            'trunk': matcher[1]
        }

    return (number_dict)


def test_fetch_details():
    assert fetch_details('499-333-5556-7333') == {'area-code': '499', 'phone-number': '5556', 'extension': '7333', 'trunk': '333'}


print(fetch_details('499-333-5556-7333'))
print(fetch_details('416-789-5308'))
print(fetch_details('416 789 5308'))
print(fetch_details('416.789.5308'))
print(fetch_details('(416) 789-5308'))
print(fetch_details('1-416-789-5308'))
print(fetch_details('416-789-5308-1111'))
print(fetch_details('416-789-5308x1111'))
print(fetch_details('416-789-5308 ext. 1111'))
