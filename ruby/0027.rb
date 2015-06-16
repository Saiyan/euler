
load 'functions.rb'

largest = 0
prod = 0

(-999..999).each do |a|
  (-999..999).each do |b|
    n=0
    while(TRUE) do
      x = n*n + a*n + b
      if x.is_prime()
        if n > largest
          largest = n
          prod = a * b
          puts "a: #{a} b: #{b} n:#{n}"
        end
        n+=1
      else
        break
      end
    end
  end
end

puts "largest: #{largest} prod: #{prod}"