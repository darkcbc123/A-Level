sizes = { 'international': ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL'],
          'Ukraine': ['42', '44', '46', '48', '50', '52', '54', '56'],
          'Germany': ['36', '38', '40', '42', '44', '46', '48', '50'],
          'USA': ['8', '10', '12', '14', '16', '18', '20', '22'],
          'France': ['38', '40', '42', '44', '46', '48', '50', '52'],
          'GB': ['24', '26', '28', '30', '32', '34', '36', '38']}
          
          

          
country = input('Enter the contry to convert:   ')
size = input('Enter the size:   ').upper()

def find_new_size(country, size):
    
    count = 0
    for i in sizes['international']:
        count += 1
        if i == size:
            number_of_elem = count
    
    return print(F'The {country} size is {sizes[country][number_of_elem - 1]}')
        
find_new_size(country, size)       
    
