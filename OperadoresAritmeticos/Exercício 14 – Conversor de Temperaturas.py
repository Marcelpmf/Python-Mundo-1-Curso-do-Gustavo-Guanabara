celsius = float(input('Digite a temperatura em °C: '))

far = 9 * celsius / 5 + 32 # pode deixar sem () pq a ordem ta ok

print('A temperatura de {}°C corresponde a {}°F'.format(celsius, far))