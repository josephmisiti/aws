#### What is this ?

It is yet another script / program / whatever that can be used to interface
with amazon ec2. It uses boto to create the command line interface.

#### Examples

List all instances:

```
$ python ec2.py -l

r-xxxxxxxx -{u'Name': u'STAGING.EXAMPLE.COM'}
r-xxxxxxxx -{u'Name': u'DEEP LEARNING'}
r-xxxxxxxx -{u'Name': u'EXAMPLE.COM'}
r-xxxxxxxx -{u'Name': u'TESTER'}
r-xxxxxxxx -{u'Name': u'EXAMPLE.COM'}
r-xxxxxxxx -{u'Name': u'BETA.EXAMPLE.COM'}

```

Start an instance:

```
$python ec2.py --instance-id i-XXXXXXX --instance-state start
```

Stop an instance:

```
$python ec2.py --instance-id i-XXXXXXX --instance-state stop
```