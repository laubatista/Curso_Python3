medida = float(input('Digite a distância de metros'))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida/ 100
km = medida / 1000

print('A distância de {}m equivale a:\ndecímetro = {:.0f}\ncentímetros = {:.0f}\nmilímetros = {:.0f}\ndecâmetro = {:.0f}\nhectômetro = {:.0f}\nkilômetro = {:.0f}'. format(medida,dm, cm, mm, dam, hm, km))





