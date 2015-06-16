require 'bigdecimal'

def get_largest_cycle(str)
  subs = []
  chars = ""
  largest = ""
  (0..(str.length-1)).each do | i |
    chars=""
    (i..(str.length-1)).each do | j |
      chars.concat(str[j])
      subs.push(chars)
      if subs.include?(chars)
        s = str.scan(/#{chars}/).size
        if s != nil and s > 1
          largest = chars
        end
      end
    end
  end
  return largest
end

largest = ""
d = 0

(2..10).each do | i |
  x = BigDecimal.new(1) / i
  x = x.to_s.gsub("0.","").gsub(/0+$/,"").gsub("E","")
  c = get_largest_cycle(x)
  #puts "x:#{x} c:#{i}"
  if c.length > largest.length
    largest =  c
    d = i
    puts "largest: #{largest.length}"
    puts "d:#{d}"
    puts "x: #{x}"
  end 
end
