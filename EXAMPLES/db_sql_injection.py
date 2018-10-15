#!/usr/bin/env python
#
good_input = 'Google'
malicious_input  = "'; drop table customers; -- "  # <1>

naive_format = "select * from customers where company_name = '{}' and company_id != 0"

good_query = naive_format.format(good_input)  # <2>
malicious_query = naive_format.format(malicious_input)  # <2>

print("Good query:")
print(good_query)  # <3>
print()

print("Bad query:")
print(malicious_query)  # <4>



