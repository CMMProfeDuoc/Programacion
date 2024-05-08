lista = [
    8 , 3 , 10 , 10 , 9 , 9 , 9 , 8 , 2 , 9 , 8 , 0 , 8 , 2 , 5 , 5 , 0 , 4 , 1 , 3 , 0 , 7 , 5 , 5 , 10 , 7 , 6 , 5 , 10 , 6
]

(0..lista.size).each do |i|
  (i+1..lista.size).each do |j|
    lista[i] > lista[j] ? lista[i],lista[j] = lista[j],lista[i] : next
  end
end
