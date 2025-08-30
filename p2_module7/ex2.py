#filter word with len>specified
"Hello Python.This is converted text."

text="Hello Pithon. This is converted text."
def get_long_words(text_var:str,length:int) ->list:
     return list(
         filter(
             lambda x:len(x) > length,
             map(lambda _: _.strip(",.;:"),text_var.split()),
         )
     )

print(get_long_words(text,3))
