my @values = (1,7,6,2,9,8,2,0,2,0);
 
my %count;
 
foreach my $num (@values) {
    $count{$num}++;
}
 
foreach my $num (sort keys %count) {
    printf "%-3s %s\n", $num, $count{$num};
}