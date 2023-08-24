def valid_email(email):
  
  k = 0
  if len(email) >= 6:
    if email[0].isalpha():
      if ('@' in email) and (email.count('@') == 1):
        if (email[-4] == '.') ^ (email[-3] == '.'):  # XOR operator - true true gives false, false false gives false else gives true
          for i in email:
            if i.isspace():
              k = 1
            elif i.isdigit() or i.isalpha() or i == '_' or i == '.' or i == '@':
              continue
            else:
              print("other special charaters not allowed")
          if k ==1:
            print("Wrong Email - space is there ")
          else:
            print("Right email!!")
        else:
          print("'.' is not there")
      else:
        print("'@' error")
    else:
      print("first character should be alphabet")
  else:
    print("wrong email!! Length should be graeater than 5")
  


if __name__=='__main__':
  email = input("Enter your Email: ")
  valid_email(email.lower())
