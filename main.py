def main():
        path = "books/frankenstein.txt"
        txt = get_book_text(path)
        wordcount = get_wordcount(txt)
        charcount = get_character_count(txt)
        print_book_report(path, wordcount, charcount)

def get_book_text(p):
     with open(p) as f:
        return f.read()
      
def get_wordcount(text):
    return len(text.split())

def get_character_count(text):
     text = text.lower()
     chardict = {}
     for i in text:
          if(i in chardict):
               chardict[i] += 1     
          else:
               chardict[i] = 1
     return chardict

def print_book_report(path, wordcount, char_dict):
     print(f"--- Begin report of {path} ---")
     print(f"{wordcount} words found in the document")

     sorted_dict = sorted(char_dict.items(),key=lambda item: item[1],reverse=True)
     for i in sorted_dict:
          if(i[0].isalpha()):
               print(f"The '{i[0]}' character was found {i[1]} times")

     print("--- End report ---")

     

main()