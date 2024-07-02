from random import choice, randint

def get_response(user_input: str) -> str:
    capital=0
    lowered: str=user_input.lower()
    for i in range(0,len(user_input)-1):
        if not user_input[i]==lowered[i]:
            capital=capital+1
    if 2*capital>len(user_input):
        return 'stop screaming goddammit'
    if lowered=='die':
        return 'thats not very kind'
    elif 'orz' in lowered:
        return '-1000 aura'
    elif 'd6' in lowered:
        return randint(1,6)
    elif 'im' in lowered:
        for i in range(0,len(lowered)-1):
            if lowered[i]=='i':
                if not i==len(lowered)-1:
                    if lowered[i+1]=='m':
                        if lowered[i+2]==' ':
                            return 'Hi '+lowered[i+3:]+', im Steven'
                        elif lowered[i+2]>len(lowered)-1:
                            return 'Hi '+lowered[i+3:]+', im Steven' 
                        else:
                            return 'Hi '+lowered[i+2:]+', im Steven'
    elif 'hi steven' in lowered:
        return 'no u'
    elif 'fuck' in lowered:
        return 'thats not a kind word'
    elif 'shit' in lowered:
        return 'thats not a kind word'    
    else:
        x=0