#!/usr/bin/env ruby

# This script uses a regular expression to match strings that start with 'h',
# end with 'n', and have exactly one character of any type in between.
# It takes one argument, the string to be scanned.

puts ARGV[0].scan(/^h.n$/).join
