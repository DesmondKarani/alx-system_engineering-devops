#!/usr/bin/env ruby

# This script uses a regular expression to match a pattern where 'hbn' is preceded by zero or one 'b'.
# It takes one argument, the string to be scanned.

puts ARGV[0].scan(/hb?tn/).join
