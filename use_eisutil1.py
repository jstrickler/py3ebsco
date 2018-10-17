#!/usr/bin/env python

# from pkg.pkg.pkg import module
from ebsco.eis.cm import eisutil

eisutil.check_ids()
eisutil.parse_marc()

# starts with _
# eisutil._validate_id()
