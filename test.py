badwords = ['редиска','СВО','дед','петрушка']
text ='Один редиска решил сказать дед, зачем ты начал СВО, а его посадили, теперь он петрушка'

print(' '.join(['*' * len(i) if i in badwords else i for i in text.split()]))