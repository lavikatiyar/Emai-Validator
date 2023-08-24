def valid_email(email):

  k = 0
  if len(email) >= 6:
    if email[0].isalpha():
      if ('@' in email) and (email.count('@') == 1):
        if (email[-4] == '.') ^ (
            email[-3] == '.'
        ):  # XOR operator - true true gives false, false false gives false else gives true
          for i in email:
            if i.isspace():
              k = 1
            elif i.isdigit() or i.isalpha(
            ) or i == '_' or i == '.' or i == '@':
              continue
            else:
              return("special charaters are not allowed")
          if k == 1:
            return("Wrong Email, space is there")
          else:
            return ("Right email!!")
        else:
          return("'.' is not there")
      else:
        return("'@' error")
    else:
      return("first character should be alphabet")
  else:
    return("Length should be graeater than 5")
