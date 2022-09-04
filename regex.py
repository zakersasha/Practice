import re

a = 'officialonlyfanspremiu,  213i7_________________, dAAEoXA5cq-9VCn8mJtWig'
d = re.findall(r"(?=[^ ]*[A-Z])(?=[^ ]*[0-9])([\w\-]{22})", a)
print(d)
