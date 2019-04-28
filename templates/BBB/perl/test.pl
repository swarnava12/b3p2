#!/usr/bin/perl

print "Content-type:text/html\r\n\r\n";
print '<html>';
print '<head>';
print '<title>Hello Word - First CGI Program</title>';
print '</head>';
print '<body>';
print '<h2>Hello Word! This is my first CGI program</h2>';
print '</body>';
print '</html>';
$x =8;
$y =10;
#print ($x+$y);

my $output = system("1.py", $out);
print "$output";
print "$out[0]";


1;
