#!/usr/bin/env ruby

# This script uses a regular expression to match only the capital letters in a given string.
# It takes one argument, the string to be scanned.

puts ARGV[0].scan(/[A-Z]/).join
