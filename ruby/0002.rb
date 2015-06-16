summe = 0
fib = 0
x = 1
y = 1

while fib < 4000000
  fib = x+y
  x = y 
  y = fib
  if fib % 2 == 0
    summe+=fib
  end
end

puts summe