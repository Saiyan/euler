def fizzbuzz?(i)
  res=""
  if i % 3 == 0
    res+="fizz"
  end
  if i % 5 == 0
    res+="buzz"
  end
  return res
end

a=""
i=0
while (a = gets) != "\n"
  i = a.to_i
  if i != nil
    s = fizzbuzz?(i)
    
    puts s != "" ? s : i  
  end
end