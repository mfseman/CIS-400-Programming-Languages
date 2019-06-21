use strict;
use warnings;

  print 'Enter your Input: ';
 
  my $valInput = <STDIN>;
  #my @StringVal = (['Yes'], ['yEs'], ['yeS'], ['YEs'], ['YeS'], ['yes'], ['yES'], ['YES']);
  my $StringVal2 = "the";
  
# Letter Patter for a - odd followed by even
	if ($valInput  =~/^-?\d+$/)
	{
		# use split the value into smaller sections if its a two digit value
		my @char = split //, $valInput;
		# If the value's first double digit value remainder is one when the module
		# is divisable by two. the single digit must also be divisable by 2 and have the mode of 0
		if($char[0] %2 == 1 && $char[1]%2 == 0)
		{
	    print "Odd digit followed by even digit";
		}
	}
# Letter Patter for b - letter followed by non letter
	if ($valInput  =~/[a-z]/ and $valInput =~/\W/ and $valInput =~ /^-?d+$/)
	{
	    print "A word that starts with a non letter followed by num";
	}
# Letter Patter for c - word starting with uppercase
	if ($valInput  =~/^[A-Z]/)
	{
		print "A word that starts with an upper case letter  \n";
	}
	# Letter Patter for d - "yes" is in string
	
	if ($valInput =~ "Yes" or $valInput =~ "Yes" or $valInput =~ "yEs" or $valInput =~ "yeS" or $valInput =~ "YEs" or $valInput =~ "YeS" or $valInput =~ "yes" or $valInput =~ "yES" or $valInput =~ "YES")
	{
	      print "Yes is in string";
	}
# Letter Patter for e - "the" was used one or more times

	if ($valInput  =~ /\Q$StringVal2\E/) # The
	{
		print "the was found";
	}
# Letter Patter for f - Date
	if ($valInput  =~ /[0-9]{2}.[0-9]{2}/)
	{
	print "Youre in date\n";
	}
# Letter Patter for g - Punctuation Mark
	if ($valInput  =~ s/[[:punct:]]//g)
	{
	print "punctuation found\n";
	}