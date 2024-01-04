#!/usr/bin/env ruby

# This script uses a regular expression to match a pattern where 'hbn' is preceded by zero or more 't's,
# but it does not match if 'o' appears between 'hb' and 'n'.
# It takes one argument, the string to be scanned.

puts ARGV[0].scan(/hbt*n/).join
