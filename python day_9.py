capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'germany':'Berlin'})
capitals.pop('China')
capitals.update({'USA':'New York'})
print(capitals.get('Russia'))

print(capitals.keys())