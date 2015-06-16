largest = 0;
for i in 100..999
  for j in 100..999
    x =  i * j
    if "#{x}" == "#{x}".reverse and x > largest
       largest = x
    end
  end
end

puts largest