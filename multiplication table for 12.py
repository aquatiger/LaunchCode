# multiplication table of 12s
#the first section is my code which doesn't really work

for i in range(1, 13):
    for j in range(1, 13):
        print('{} {}'.format(i*j, "\t"))
    print()

"""
got this online and it works, which doesn't always happen.
The guy says this is an advanced trick, but given the instructions
I suspect they wanted us to use a format method, but I can't think
of how to do this or why the : works even though it is used in the
instructions, not really explained. And also when you run the following
code you get nicely spaced results even though there are sometimes
2 and sometimes 3 digits. Also not sure what the * does in the print.

"""
##for row in range(1,13):
##    print(*("{:5}".format(row*col) for col in range(1, 13)))
    
