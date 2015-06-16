
class Fixnum
  def is_divisor_of(n)
    return n % self == 0
  end
  
  def is_prime()
    i = self.abs
    (2..i/2).each do |x| 
      if i % x == 0
        return false
      end
    end
    return true
  end





  def is_mirp()
    i = self
    if is_prime i and "#{i}".reverse != "#{i}" and is_prime "#{i}".reverse.to_i
      return true
    end
    return false
  end

  def get_divisors()
    divs = []
    (1..self/2).each do |i|
      if i.is_divisor_of(self)
        divs.push(i)
      end
    end
    return divs
  end
  
  def is_abundant()
    divs = self.get_divisors()
    summe=0
    divs.each {|i| summe+= i}
    return summe > self
  end
end
