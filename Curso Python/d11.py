larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
total = area / 2
print('Sua parede possui dimensões de {}X{} e a área de {}m². /m E com essa área você irá precisar de {} litros para pintar essa parede'.format(larg, alt, area, total))
