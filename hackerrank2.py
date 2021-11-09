a="sameendra"
print("hi %s i am loving the stay here"%a)

import re
v = "aeiou"
c = "^aeiou"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))
