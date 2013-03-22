#! /usr/bin/perl -w

opendir(DIR, "$ARGV[0]");

@FILES = readdir DIR;

closedir(DIR);

foreach $file (@FILES){
    if($file =~ /earthquake\_.*\.txt/){
	$output = $file;
	$output =~ s/\.txt/\.data/g;
	`perl -CS /home/qmei/qmei/src/Twitter/earthquake_parser_simple.pl $ARGV[0]/$file > $output`;
    }
}
