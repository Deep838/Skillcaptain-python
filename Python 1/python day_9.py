capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'germany':'Berlin'})
capitals.pop('China')
capitals.update({'USA':'New York'})
print('Russia' in capitals)

print(capitals.keys())