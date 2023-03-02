#!/usr/bin/env ruby

current_text = ''

loop do
  # selected_text = %x[xsel -o].to_s.strip
  selected_text = %x[xclip -o -sel c].to_s.strip
  if (current_text != selected_text)
    current_text = selected_text
    puts %x[xsel -o | trans :ru ]
    sleep 8
  end
end
