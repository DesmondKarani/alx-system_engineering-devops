#!/usr/bin/env ruby

# This script uses a regular expression to match a pattern where 'hbn' is preceded by one or more 't's.
# It takes one argument, the string to be scanned.

puts ARGV[0].scan(/hbt+n/).join
