from binarytree import Node as N

print(N("B"))
print(N("C", N("D")))
print(N("E", N("F"), N("G", N("H"))))
print(N(1, N(2, N(4, N(8), N(9)), N(5)), N(3, N(6, N(10), N(11)), N(7, N(12)))))
print(N("A", N("B"), N("C", N("D", N("E")))))
print(N("F", N("G"), N("H", N("I", N("J")))))
print(N("A", N("B"), N("C", N("D"), N("E"))))
print(N(1, N(2, N(4, N(8), N(9)), N(5, N(10), N(11))), N(3, N(6, N(12), N(13)), N(7))))

amar = N("Amar")
janak = N("Janak")
raj = N("Raj")
pallav = N("Pallav")
deepak = N("Deepak")
sanjay = N("Sanjay")
rudraksh = N("Rudraksh")
ridhiman = N("Ridhiman")
tanush = N("Tanush")
kuvam = N("Kuvam")
kunsh = N("Kunsh")

amar.left = janak
amar.right = raj
janak.left = pallav
pallav.left = rudraksh
raj.left = deepak
raj.right = sanjay
deepak.left = ridhiman
deepak.right = tanush
sanjay.left = kuvam
sanjay.right = kunsh

print(amar)
