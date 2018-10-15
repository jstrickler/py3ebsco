#!/usr/bin/env python
'''Use etree navigation to extract planets from solar.xml'''
import lxml.etree as ET

def main():
    '''Program entry point'''
    doc = ET.parse('../DATA/solar.xml') # <1>
    
    solar_system = doc.getroot()  # <2>
    
    print(solar_system)
    print()
    
    inner = solar_system.find('innerplanets') # <3>
    print('Inner:')
    
    for planet in inner:  # <4>
        if planet.tag == 'planet':
            print('\t', planet.get("name", "NO NAME"))
            
    outer = solar_system.find('outerplanets')
    print('Outer:')
    
    for planet in outer:
        print('\t', planet.get("name"))
            
    plutoids = solar_system.find('dwarfplanets')
    print('Dwarf:')
    
    for planet in plutoids:
        print('\t', planet.get("name"))

if __name__ == '__main__':
    main()
