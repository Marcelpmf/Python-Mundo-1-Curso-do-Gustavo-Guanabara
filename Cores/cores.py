# ANSI (escape sequence) \033[ (codico da cor) m

# \033[ (estilo da fonte)(cor do texto)(background cor de fundo) m

# \033[0:33:44m

# estilo da fonte: 0 = nome / 1 = negrito / 4 = sublinhado / 7 = inverte config (melhores no python)

# cor do texto: 30 = branco / 31 = verm / 32 = verd / 33 = amare / 34 = azul / 35 / 36 / 37 = cinza (padrao)

# background: 40 / 41 / 42 / 43 / 44 / 45 / 46 / 47 (mesma coisa de texto)


print('\33[7;33;44mOlá, mundo!\33[m')

a = 5
b = 9

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a ,b))

nome = 'anteteguemon'

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:30m'}

print('Olá! muito prazer em te conhecer, {} {} {}!'.format(cores['amarelo'], nome, cores['limpa']))






