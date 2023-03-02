'''
Find the range using dictionary to return values
'''

def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    # Find teh range
    r = highest - lowest
    return {'lowest': lowest, 'highest': highest, 'range': r}

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    result = find_range(donations)
    print(f"\n\tLowest: {result['lowest']}\n\tHighest: {result['highest']}\n\tRange: {result['range']}")
