#!/usr/bin/perl 
use List::Util qw( min max );

while(@ARGV) {
    $arg = shift @ARGV;
    if($arg eq '-h') { 
            print << "help_text";
This program reads fasta formated sequence files from either a file or
from stdin and writes to stdout the maximal percentage of any character
ignoring any sites that are gapped.

    Syntax: fasta2proportion file

    Output is a list of site number, number of taxa, max percent

help_text
            exit(1); next; }

   open(FILE, $arg) || die "Error: Can't open file $arg\n";
   $i=-1;
   $a=0;
   while (<FILE>) {
    # pid line
    # chop is strip()
    # store p_id in title[]
    # store each sequence in seq[]
     if(/^>/) { $i++; chop $_; $title[$i]=$_; 
         $title[$i]=~ s/^> //; 
         $title[$i]=~ s/^>//; 
         $len=length($title[$i]);
         if($len <10) { for($j=0; $j < 9-$len; $j++) { $title[$i] .= " ";}}
         else { $title[$i] = substr($title[$i],0,10);}
         print "title i is $title[$i]\n"
     }
     elsif ($_ =~ /\s*(\d+)\s+(\d+)/){ $line = $_; print STDOUT "line is $line\n";}
     else {$seq[$i] .= $_; chop $seq[$i]; 
		$size[$i]=length($seq[$i]);
    print STDOUT "seq i is $seq[$i]\n";
     }
     if ($size[$i] > $a){
  	 $a = $size[$i];
     }
   }
   # $a is the max length of all sequences
   close(FILE);
   # species: num of sequences
   $species = ($i+1);
   $printed_error=0;
   for($j=0; $j<=$i; $j++) {
       if($seq[$j] =~ /[^ACDEFGHIKLMNPQRSTUVWYacdefghiklmnpqrstuvwy\-\.]/)
       {  print STDERR "Warning: seq number #$j; entitled $title[$j] has unknown characters \n $seq[$j] \n\n";}
   }

   # check if al sequences have the same length as $a, which is the max lenght of all sequences
   print STDOUT "   $species Taxa   $a Length\n";
   for($j=0; $j<=$i; $j++) {
       $size[$j]=length($seq[$j]);
       if ($size[$j] < $a){
          if($printed_error==1) {
	      print STDERR "\nWARNING: The sequences might not be the same\n";
	      print STDERR "size!  The output assumes \n";
              print STDERR "sequences to be the same length.\n";
	      $printed_error=1;
	  }
   	  print STDERR "Sequence $j, entitled $title[$j] has length $size[$j] not $a.\n";
       } 
   }
   # store all characters in all sequences in a 2D array seqChars
   $seqLength=$a;
   @notAminoAcids = ( "66", "74", "79", "85", "88", "90" );
   for($j=0; $j<$species; $j++) {
       @Chars = split("", $seq[$j]);
       for($i=0; $i<$seqLength; $i++) {
           $seqChars[$j][$i] = $Chars[$i];
       }
   }

# build array ordinal[], ordinal[]. The total number of each amino acids among all sequences
# n: total number of amino acids at one postions, in all sequences
# max: is the percentage of the occurance_of_the_most_occured_AA/n
   for($k=0; $k<$seqLength; $k++) {
       # ascii code 65: A - 89: Y 
       for($x=65; $x <=89; $x++) { $ordinal[$x-65]=0; }
       for($n=0, $j=0; $j<$species; $j++) { 
           # print STDOUT "looking at $j $k $seqChars[$j][$k]\n";
           $x=ord($seqChars[$j][$k]);
           # print STDOUT "looking at $x\n";
           if($x < 65) { next; }
           if($x > 89) { next; }
           if ( grep( /^$x$/, @notAminoAcids ) ) { next; }
           $n++;
           $ordinal[ord($seqChars[$j][$k])-65]++; 
       }
       $max = max(@ordinal)/$n;
       $site=$k+1;
       printf STDOUT "%6d %6d %10.4f\n", $site,$n,$max;
   }
   print STDOUT "\n";
}
