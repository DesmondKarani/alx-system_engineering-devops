#!/usr/bin/env ruby

# This script uses a regular expression to match a string that is exactly a 10-digit phone number.
# It takes one argument, the string to be scanned.

puts ARGV[0].scan(/^\d{10}$/).join
