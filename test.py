# the iso in use here was created by doing this:
#
# $ mkdir tmp
# $ echo foo > tmp/foo
# $ genisoimage -v -v -iso-level 1 -no-pad -o test.iso tmp
#
# It seems to be about the smallest ISO that you can make

import pyiso

iso = pyiso.PyIso()
iso.open('test.iso')
iso.print_tree()
iso.close()
