#!/usr/bin/env ruby

# Check if there is exactly one argument provided
if ARGV.length != 1
  puts "Usage: ruby script.rb <string>"
  exit 1
end

# Define the regular expression using Oniguruma syntax
regex = /School/

# Get the input argument
input_string = ARGV[0]

# Check if the input string matches the regex
if regex.match(input_string)
  puts "Match found: #{input_string}"
else
  puts "No match found for 'School' in #{input_string}"
end
