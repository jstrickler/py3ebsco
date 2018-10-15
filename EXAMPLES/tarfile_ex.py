#!/usr/bin/env python
import tarfile
import os

for tar_file in ('pres.tar', 'NOT_A.tar', 'potus.tar.gz'): # <1>
    filename = os.path.join('../DATA', tar_file)
    is_valid = tarfile.is_tarfile(filename) # <2>
    text = 'IS' if is_valid else 'IS NOT'
    print("{} {} a tarfile".format(filename, text))
print()

with tarfile.open('../DATA/pres.tar') as tarfile_in: # <3>
    for member in tarfile_in: # <4>
        print(member.name, member.size) # <5>
    print()

with tarfile.open('../DATA/pres.tar') as tarfile_in:
    tarfile_in.extract('presidents.txt', path='../TEMP') # <6>

with tarfile.open('../DATA/potus.tar.gz') as tarfile_in:
    tarfile_in.extract('presidents.csv', path='../TEMP') # <6>

with tarfile.open('../TEMP/text_files.tar','w') as tarfile_out: # <7>
    tarfile_out.add('../DATA/parrot.txt') # <8>
    tarfile_out.add('../DATA/alice.txt')  # <8>

with tarfile.open('../TEMP/more_text_files.tar.gz','w:gz') as TAR_GZ_WRITE: # <9>
    TAR_GZ_WRITE.add('../DATA/parrot.txt') # <8>
    TAR_GZ_WRITE.add('../DATA/alice.txt')  # <8>

