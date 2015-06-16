summe=0
(1..999).each do  |i|
  if i % 3 == 0 or i % 5 == 0
    summe+=i
  end
end

puts summe