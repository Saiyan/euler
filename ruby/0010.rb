load 'functions.rb'

summe = 2
i=3
while i < 2000000
  if is_prime i
    summe+=i
  end
  i+=2
end

puts summe