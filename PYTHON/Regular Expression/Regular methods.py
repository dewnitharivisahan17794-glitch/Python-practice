import re
#findall() method returns a list containing all matches
text = "The rain in Spain"
matches = re.findall("ai", text)
print(matches)
Emails = "Please contact us at info@example.com or support@example.com"
email_matches = re.findall(r'\w+@example.com', Emails)
print(email_matches)

#search() method returns a match object if there is a match anywhere in the string
text = "The rain in Spain"
k=input("Enter a character to search: ")
match = re.search(k, text)
if match:
    print("Match found:", match.group())
    print("Path is", match.span())
else:
    print("No match found")    

#split() method splits the string at each match and returns a list of substrings
text = "The rain in Spain"
split_text = re.split(" ", text)
print(split_text)

#sub() method replaces the matches with the text of your choice
text = "The rain in Spain"  
sub_text = re.sub(" ", "-", text)   
print(sub_text)

text = "The rain in Spain"  
sub_text = re.sub(" ", "-", text)   # replaces only the first occurrence
print(sub_text)

text = "The rain in Spain"  
sub_text = re.sub("Spain", "France", text)   
print(sub_text)