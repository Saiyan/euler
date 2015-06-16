load 'functions.rb'

nr=0
prm=0
i=2
while nr < 10001
  if(is_prime(i))
    nr+=1
    prm=i
  end
  i+=1
end

puts prm