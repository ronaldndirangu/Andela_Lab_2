def find_max_min(numbers):
  
    min_num=min(numbers)
    max_num=max(numbers)
    
    if max_num != min_num:
      return [min_num,max_num]
    else:
      return [len(numbers)]
