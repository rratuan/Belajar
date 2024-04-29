t = int(input('masukkan tinggi segitiga : '))

#right triangle
# preview
# +         => i(1)
# ++        => i(2)
# +++       => i(3)
# ++++      => i(4)
# +++++     => i(5)
for i in range(1,t+1):
    print(i * '+')

print('\n')

# right downward triangle
# preview 
# +++++ => i(1) = 5 
# ++++  => i(2) = 4
# +++   => i(3) = 3
# ++    => i(4) = 2 
# +     => i(5) = 1
# rumus = t-i+1
for i in range(1,t+1):
    print('+' * (t-i+1))

print('\n')

# pyramid
# preview
#     +     => i(1) = 1 ---- spasi = 4
#    +++    => i(2) = 3 ---- spasi = 3
#   +++++   => i(3) = 5 ---- spasi = 2
#  +++++++  => i(4) = 7 ---- spasi = 1
# +++++++++ => i(5) = 9 ---- spasi = 0
# spasi = t-i
# rumus = 2*i-1
for i in range(1,t+1):
    print(' '*(t-i),'+'*(2*i-1))

print('\n')

# left triangle
# preview
#     + => i(1) ---spasi = 4
#    ++ => i(2) ---spasi = 3
#   +++ => i(3) ---spasi = 2
#  ++++ => i(4) ---spasi = 1
# +++++ => i(5) ---spasi = 0
# spasi = t-i
for i in range(1,t+1):
    print(' '*(t-i),i*'+')

print('\n')

# left downward triangle
# preview
# +++++ => i(1) = 5 ---spasi = 0
#  ++++ => i(2) = 4 ---spasi = 1
#   +++ => i(3) = 3 ---spasi = 2
#    ++ => i(4) = 2 ---spasi = 3
#     + => i(5) = 1 ---spasi = 4
# rumus = t-i+1
# spasi = t-6+i
for i in range(1,t+1):
    print(' '*(t-6+i),'+'*(t-i+1))

print('\n')

# reverse pyramid
# preview
# +++++++++ => i(1) = 9 ---spasi = 0
#  +++++++  => i(2) = 7 ---spasi = 1
#   +++++   => i(3) = 5 ---spasi = 2
#    +++    => i(4) = 3 ---spasi = 3
#     +     => i(5) = 1 ---spasi = 4
# rumus = (2*t) - (2*i) + 1
# spasi = i-1
for i in range(1,t+1):
    print(' '*(i-1),'+'*((2*t)-(2*i)+1))

print('\n')

# diamond
# preview
#     +     => i(1) = 1 ---spasi = 4
#    +++    => i(2) = 3 ---spasi = 3
#   +++++   => i(3) = 5 ---spasi = 2
#  +++++++  => i(4) = 7 ---spasi = 1
# +++++++++ => i(5) = 9 ---spasi = 0
#  +++++++  => j(1) = 7 ---spasi = 1
#   +++++   => j(2) = 5 ---spasi = 2
#    +++    => j(3) = 3 ---spasi = 3
#     +     => j(4) = 1 ---spasi = 4
# rumus i = 2*i-1
# rumus j = (2*t) - (2*j) + 1
# spasi i = t-i
# spasi j = j-1
for i in range(1,t+1):
    print(' '*(t-i),'+'*(2*i-1))
    if i == t:
        for j in range(2,t+1):
            print(' '*(j-1),'+'*((2*t)-(2*j)+1))

print('\n')


