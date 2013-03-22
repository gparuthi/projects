#! /usr/bin/perl -w                                                            

use JSON;
use Encode;

if($#ARGV < 0){
    die "Usage: perl -CS $0 raw_sample_file > output_every_thing";
}

open(IN, $ARGV[1]);

while($line = <IN>){
    chomp $line;
    $kw{"$line"} = 1;
}
close(IN);

open(IN, $ARGV[0]);

$pos = 0;

my $tweet;
my $src;
my %field;

while($line = <IN>){
#    $line = <IN>;
    
    chomp $line;
#    $src = Encode::decode_utf8($line);
    
    $src = $line;
    %field = ();
    
    $pos ++;
    if($pos % 100000 == 0){
        print STDERR "$pos tweets processed... \n";
    }
    
    $tweet = from_json($src);
    
#   if(exists $tweet->{user}->{lang} && $tweet->{user}->{lang} eq "en"){
#    &parse_ht($tweet, "tweet");
    &output($tweet);
    
#    print "\n\n";
    
}

close(IN);

sub output {
    my $tweet = shift;
    my $i;
    my $flag = 0;
    if(defined $tweet->{text}){
	@w = split(/\s/, $tweet->{text});
	foreach $key (@w){
	    if(defined $kw{"$key"}){
		$flag = 1;
		last;
	    }
	}
    }
    if($flag == 0){
	return;
    }
    if(defined $tweet->{text}){
	printf "ID\t%s\n", $tweet->{id};
        printf "User\t%s\n", $tweet->{user}->{screen_name};
        printf "Text\t%s\n", $tweet->{text};
        printf "Time\t%s\n", $tweet->{created_at};
    }
    else{
	return;
    }
    if(defined $tweet->{coordinates}){
        printf "Coordinates\t%s, %s\n", $tweet->{coordinates}->{coordinates}->[0], $tweet->{coordinates}->{coordinates}->[1];
    }
    if(defined $tweet->{place}){
        printf "Place\t%s, %d\n", $tweet->{place}->{full_name}, $#{$tweet->{place}->{bounding_box}->{coordinates}->[0]};
    }
    if(defined $tweet->{geo}){
        printf "Geo\t%s, %s\n", $tweet->{geo}->{coordinates}->[0], $tweet->{geo}->{coordinates}->[1];
    }
    if(defined $tweet->{user}->{location}){
        printf "UserLocation\t%s\n", $tweet->{user}->{location};
    }
    
    if(defined $tweet->{retweeted_status}){
	printf "RetweetID\t%s\n", $tweet->{retweeted_status}->{id_str};
	printf "RetweetUser\t%s\n", $tweet->{retweeted_status}->{user}->{screen_name};
    }

    if(defined $tweet->{entities}->{urls}){
        for($i = 0; $i <= $#{$tweet->{entities}->{urls}}; $i ++){
	    printf "URL\t%s\n", ${$tweet->{entities}->{urls}}[$i]->{url};
        }
    }
    
    if(defined $tweet->{entities}->{hashtags}){
	for($i = 0; $i <= $#{$tweet->{entities}->{hashtags}}; $i ++){
            printf "HT\t\#%s\n", $tweet->{entities}->{hashtags}->[$i]->{text};
        }
    }
    
    print "\n\n";

}
