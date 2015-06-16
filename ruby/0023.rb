load 'functions.rb'

#todo: GRRRRRRRRRRRRRR

abundants = []
sum_all = 0
sum_abundants = 0
numbers = (1..28123)


numbers.each do | i |
  sum_all+=i
end

puts "Sum all complete"  

numbers.each do |i|
  if i.is_abundant
    abundants.push(i)
  end
end

puts "Abundants loaded"
puts abundants.length
abundant_sums = []

abundants.each do | a |
  abundants.each do | a2 |
    summe = a+a2
    if summe <= 28123
      abundant_sums.push(summe)
    end
  end
end

abundant_sums = abundant_sums.uniq()
  
abundant_sums.each do |i|
  sum_abundants+=i
end

puts sum_all
puts sum_abundants

puts sum_all - sum_abundants

