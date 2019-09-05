on = ":fastparrot:"
off = ":meow_party:"

a = [
    0, 1, 1, 0,
    1, 0, 0, 1,
    1, 1, 1, 1,
    1, 0, 0, 1,
    1, 0, 0, 1
]

b = [
    1, 1, 1, 0,
    1, 0, 0, 1,
    1, 1, 1, 0,
    1, 0, 0, 1,
    1, 1, 1, 1
]

c = [
    0, 1, 1, 0,
    1, 0, 0, 1,
    1, 0, 0, 0,
    1, 0, 0, 1,
    0, 1, 1, 0
]

d = [
    1, 1, 1, 0,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 1, 1, 1
]

e = [
    1, 1, 1, 1,
    1, 0, 0, 0,
    1, 1, 1, 1,
    1, 0, 0, 0,
    1, 1, 1, 1
]

f = [
    1, 1, 1, 1,
    1, 0, 0, 0,
    1, 1, 1, 0,
    1, 0, 0, 0,
    1, 0, 0, 0
]

g = [
    0, 1, 1, 0,
    1, 0, 0, 0,
    1, 0, 1, 1,
    1, 0, 0, 1,
    0, 1, 1, 0
]

h = [
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 1, 1, 1,
    1, 0, 0, 1,
    1, 0, 0, 1
]

i = [
    1, 1, 1,
    0, 1, 0,
    0, 1, 0,
    0, 1, 0,
    1, 1, 1,
]

j = [
    1, 1, 1, 
    0, 1, 1, 
    0, 1, 1, 
    0, 1, 1, 
    1, 1, 0, 
]

k = [
    1, 0, 0, 1,
    1, 0, 1, 0,
    1, 1, 0, 0,
    1, 0, 1, 0,
    1, 0, 0, 1
]

l = [
    1, 0, 0, 0,
    1, 0, 0, 0,
    1, 0, 0, 0,
    1, 0, 0, 0,
    1, 1, 1, 1
]

m = [
    1, 0, 0, 0, 1,
    1, 1, 0, 1, 1,
    1, 0, 1, 0, 1,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
]

n = [
    1, 0, 0, 0, 1,
    1, 1, 0, 0, 1,
    1, 0, 1, 0, 1,
    1, 0, 0, 1, 1,
    1, 0, 0, 0, 1,
]

o = [
    0, 1, 1, 0,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    0, 1, 1, 0
]

p = [
    1, 1, 1, 0,
    1, 0, 0, 1,
    1, 1, 1, 1,
    1, 0, 0, 0,
    1, 0, 0, 0
]

q = [
    0, 1, 1, 0,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 0, 1, 1,
    0, 1, 1, 1
]

r = [
    1, 1, 1, 0,
    1, 0, 0, 1,
    1, 1, 1, 0,
    1, 0, 0, 1,
    1, 0, 0, 1
]

s = [
    0, 1, 1, 1,
    1, 0, 0, 0,
    0, 1, 1, 0,
    0, 0, 0, 1,
    1, 1, 1, 0
]

t = [
    1, 1, 1,
    0, 1, 0,
    0, 1, 0,
    0, 1, 0,
    0, 1, 0,
]

u = [
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    0, 1, 1, 0
]

v = [
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 0, 0, 1,
    0, 1, 1, 0
]

w = [
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    1, 0, 1, 0, 1,
    1, 0, 1, 0, 1,
    0, 1, 0, 1, 0,
]

x = [
    1, 0, 0, 0, 1,
    0, 1, 0, 1, 0,
    0, 0, 1, 0, 0,
    0, 1, 0, 1, 0,
    1, 0, 0, 0, 1,
]

y = [
    1, 0, 0, 1,
    1, 0, 0, 1,
    1, 1, 1, 1,
    0, 0, 0, 1,
    1, 1, 1, 1
]

z = [
    1, 1, 1, 1,
    0, 0, 1, 0,
    0, 1, 0, 0,
    1, 0, 0, 0,
    1, 1, 1, 1
]

space = [
    0, 0, 0, 0, 
    0, 0, 0, 0, 
    0, 0, 0, 0, 
    0, 0, 0, 0, 
    0, 0, 0, 0, 
]

letter_spacing = 1

glyph_height = 5

chars = 'abcdefghijklmnopqrstuvwxyz '
glyphs = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,space]


def get_glyph_for_char(char):
    i = chars.index(char)
    g = glyphs[i]
    return g

def create_str_from_glyph(glyph):
    str = ''
    glyph_width = int(len(glyph) / glyph_height)

    for y in range(glyph_height):
        for x in range(glyph_width + letter_spacing):
            #spacing
            if x >= glyph_width:
                str += off
                continue

            #char content
            i = glyph_width * y + x
        
            if glyph[i] == 1:
                str += on
            else:
                str += off
        str += '\n'

    return str
    


input_text = input('give text: ')

lines = ['' for i in range(glyph_height)]

for c in input_text:
    g = get_glyph_for_char(c)
    s = create_str_from_glyph(g)

    str_lines = s.split('\n')

    for l in range(glyph_height):
        lines[l] += str_lines[l].rstrip()
    
output = '\n'.join(lines)

print(output)
input()