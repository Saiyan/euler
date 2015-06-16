
c=0
i=0
while c != 20 do
  c=0
  i+=20
  if i % 1000000 == 0
    puts i
  end
  for j in 1..20
    if i % j == 0
      c+=1
    else
      break
    end
  end
end

puts i