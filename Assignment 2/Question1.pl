use strict;
use warnings;
print "Enter a Valid IP Address: ";


my $entry = <STDIN>;
chomp $entry;

print "You have entered '$entry'\n";

# test whether the IP address is whithin range
if($entry =~ /(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,5}\:\d{1,5})/)
  {
      print "This is a valid IP Address: $entry";
  }
 #if test is not within range, let user know
else
{
	print "You did not enter a Valid IP Address"
}

<>;