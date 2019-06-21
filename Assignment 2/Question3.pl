# Installed Email::Valid to read email from txt document
use Email::Valid;

open (MYFILE, 'input.txt');
my $email_file   = "output.txt"; #Export file
my $found = 0;

open(FH,'>',$email_file);
open my $outputEmail, ">",$email_file;

while (<MYFILE>) {
    chomp;
    my @words = split(' ');
    foreach my $word (@words) {  
        if(Email::Valid->address($word)) 
		{
			$found++;
			print FH "$word\n";
        }
    }
}

open(FH, '<output.txt');
my @lines = <FH>;
@lines = sort @lines;
open(FILE, "> $email_file");
print FILE @lines;