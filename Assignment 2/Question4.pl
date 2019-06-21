
print "Please Enter Your Values: ";
my $input = <>;
chomp $input;
my @strings = ($input);

for my $string (@strings) {
   my $sum;
   $sum += $_ for split(//, $string);
   print "$sum\n";
}