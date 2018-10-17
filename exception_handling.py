#!/usr/bin/env python

main_value = 23.9

other_values = [5, 8.9, 3, 0, 14.7, 'DeadBeef', 6.21]

for ov in other_values:
    try:
        result = main_value / ov
    except (ZeroDivisionError, TypeError) as err:
        print(err)
    except ValueError as err:
        print(err)
    except Exception as err:
        print("got", type(err).__name__, err)
    else:
        print("result is", result)
    finally:
        print("OK!")
