with open('text_file_for_Learning.txt') as file_object:
    lines=file_object.readlines()
    test_string=''
    for line in lines:
        test_string+=line.rstrip()
        print(test_string)


    
 #   contents=file_object.read()
    
  #  print(contents)
