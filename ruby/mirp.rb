load 'functions.rb'
(1..100).each do |i|
  if is_mirp(i)
    puts i
  end
end