

open("/Users/nschulte/git/adventOfCode2023/day_3/input") do f
  line = 0  
  while ! eof(f)           
    current_line = readline(f)          
    line += 1

    numbers_current_line = []

    current_number = -1
    for c in [filter(isdigit, collect(s)) for s in current_line] # search for any digit
      if isempty(c)
        if current_number != -1
          push!(numbers_current_line, parse(Int, current_number))
        end
        continue
      end
      # found a digit, appending it to the current number string
      current_number += c[1]
    end

    print(current_line, numbers_current_line)

    break
  end
 
end
