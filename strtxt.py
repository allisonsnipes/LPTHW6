x = "there are %d types of people." % 10
binary = 'binary'
do_not = 'dont'
y = 'those who know %s and those who %s.' % (binary, do_not)

print x
print y

print 'i said %r' % x
print 'i said %s' % y

hilarious = False
joke_evaluation = 'isnt that joke so %r'

print joke_evaluation % hilarious

w = 'this is the left side'
e = 'this is the right side'

print w + e
