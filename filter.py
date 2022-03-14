import statistics
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
media = statistics.mean(dados)
print(f'a média é {media} ')
res = filter(lambda x: x > media, dados)  # Aqui vamos filtrar valores maiores que a media.
print(list(res))
