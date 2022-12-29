import deadlock
# this will read and write the input from the terminal window
while True:
    text=input('Deadlock >>> ')
    result,error=deadlock.run('<stdin>',text)

    if error:print(error.as_string())
    else:print(result)

# lexer will go through the inputs and break them into individual items called TOKENS consisting of Type and Value1+2*5