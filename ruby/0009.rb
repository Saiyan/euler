(1..1000).each do | a |
  (1..1000).each do | b |
    (1..1000).each do | c |
      if a**2 + b**2 == c**2 and a < b and b < c and a + b + c == 1000
        puts a*b*c
        exit
      end
    end
  end
end

