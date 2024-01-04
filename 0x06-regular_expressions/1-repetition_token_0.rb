#!/usr/bin/env ruby

# This script matches a pattern where 'hbt' is followed by 2 to 5 't's and then 'n'.
# It takes one argument, the string to be scanned.

puts ARGV[0].scan(/hbt{2,5}n/).join
