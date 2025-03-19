def num_ips(ip1, ip2):
    ip1 = ip1.split('.')
    ip2 = ip2.split('.')

    substract = ((int(ip2[0]) * 256 ** 3 + int(ip2[1]) * 256 ** 2 + int(ip2[2]) * 256 + int(ip2[3])) -
        (int(ip1[0]) * 256 ** 3 + int(ip1[1]) * 256 ** 2 + int(ip1[2]) * 256 + int(ip1[3])))

    return substract


ip1 = input()
ip2 = input()

print(num_ips(ip1, ip2))
