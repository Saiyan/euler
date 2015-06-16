load 'functions.rb'

def get_prime_factors (n)
  facts = Array.new
  for i in 2..n/2
    if n % i == 0 and is_prime(i)
      facts.push(i)
    end
  end
  puts facts.length()
  return facts
end

facts = get_prime_factors(600851475143)
puts facts[-1]