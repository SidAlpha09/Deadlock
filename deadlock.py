###############
#CONSTANTS
###############
DIGITS = '0123456789'

###############
#ERROR
###############

class Error:
    def __init__(self,pos_start,pos_end,error_name,details):
        self.pos_start=pos_start
        self.pos_end=pos_end
        self.error_name=error_name
        self.details=details

    def as_string(self):
        result = f'{self.error_name}:{self.details} \n'
        result+=f'File{self.pos_start.fn},line{self.pos_start.line + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self,pos_start,pos_end, details):
        super().__init__(pos_start,pos_end,'Illegal Character',details)

class Position:
    def __init__(self,index,line,col,fn,ftxt):
        self.index=index
        self.line=line
        self.col=col
        self.fn=fn
        self.ftxt=ftxt
    
    def advance(self,current_char):
        self.index +=1
        self.col +=1

        if(current_char =='\n'):
            self.line +=1
            self.col =0

        return self

    def copy(self):
        return Position(self.index,self.line,self.col,self.fn,self.ftxt)
       
        

   
###############
#TOKENS
###############
DD_INT      = 'INT'
DD_FLOAT    = 'FLOAT'
DD_PLUS     = 'PLUS'
DD_MINUS    = 'MINUS'
DD_MUL      = 'MUL'
DD_DIV      = 'DIV'
DD_MOD      = 'MOD'
DD_LPREN    = 'LPREN'
DD_RPREN    = 'RPREN'

class Token:
    def __init__(self,type_,value=None):
        self.type=type_
        self.value=value
    def __repr__(self):
        if self.value:return f'{self.type}:{self.value}'
        return f'{self.type}'


#################
#LEXER
#################

class Lexer:
    def __init__(self,fn,text):
        self.fn=fn
        self.text=text
        self.pos=Position(-1,0,-1,fn,text)
        self.current_char=None
        self.advance()
    
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char=self.text[self.pos.index] if self.pos.index<len(self.text) else None

    def make_tokens(self):
        tokens=[]

        while self.current_char !=None:
            #for spaces
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char =='+':
                tokens.append(Token(DD_PLUS))
                self.advance()
            elif self.current_char =='-':
                tokens.append(Token(DD_MINUS))
                self.advance()
            elif self.current_char =='*':
                tokens.append(Token(DD_MUL))
                self.advance()
            elif self.current_char =='/':
                tokens.append(Token(DD_DIV))
                self.advance()
            elif self.current_char =='%':
                tokens.append(Token(DD_MOD))
                self.advance()
            elif self.current_char =='(':
                tokens.append(Token(DD_LPREN))
                self.advance()
            elif self.current_char ==')':
                tokens.append(Token(DD_RPREN))
                self.advance()
            else:
                #return some error

                pos_start=self.pos.copy()
                char=self.current_char
                self.advance()
                return [],IllegalCharError(pos_start,self.pos,"'"+char+"'")

        return tokens , None


    def make_number(self):
        num_str =''
        dot_count=0

        while self.current_char !=None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1:break
                dot_count+=1
                num_str+='.'
            else:
                num_str+=self.current_char
            self.advance()
        
        if dot_count==0:
            return Token(DD_INT,int(num_str))
        else:
            return Token(DD_FLOAT,float(num_str))

#########################
#NODES
#########################

class NumberNode:
    def __init__(self,tok):
        self.tok=tok
        
    def __repr__(self):
        return f'{self.tok}'

class BinOpNode:
    def __init__(self,left_node,op_tok,right_node):
        self.left_node=left_node
        self.op_tok=op_tok
        self.right_node=right_node

    def __repr__(self):
        return f'({self.left_node},{self.op_tok},{self.right_node})'

#########################
#PARSER
#########################

class Parser:
    def __init__(self,tokens):
        self.tokens=tokens
        self.tok_idx=1
        self.advance()

    def advance(self):
        self.tok_idx+=1
        if self.tok_idx<len(self.tokens):
            self.current_tok=self.tokens[self.tok_idx]
        return self.current_tok

########################

    def parse(self):
        res=self.expr()
        return res

    def factor(self):
        tok=self.current_tok
        if tok.type in (DD_INT,DD_FLOAT):
            self.advance()
            return NumberNode(tok)

    def term(self):
        return self.bin_op(self.factor,(DD_MUL,DD_DIV,DD_MOD))

    def expr(self):
        return self.bin_op(self.term,(DD_PLUS,DD_MINUS))

    def bin_op(self,func,ops):
        left=func()
        while self.current_tok.type in ops:
            op_tok=self.current_tok
            self.advance()
            right=func()
            left=BinOpNode(left,op_tok,right)

        return left ##it is now a binary operation node

#########################
#RUN
#########################

def run(fn ,text):
    #GENERATES TOKENS
    lexer=Lexer(fn,text)
    tokens,error=lexer.make_tokens()
    if error:return None,error

    #GENERATES THE ABSTRACT SYNTAX TREE
    parser=Parser(tokens)
    ast=parser.parse()

    return ast,None

