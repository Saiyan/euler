
sumofsq=0
sqofsum=0

for i in 1..100
  sumofsq+= i*i
end

for i in 1..100
  sqofsum += i
end 

sqofsum*=sqofsum

puts sqofsum - sumofsq