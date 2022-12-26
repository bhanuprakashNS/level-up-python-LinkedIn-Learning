given_number = int(input('Enter a number?'))

def find_prime_factors(number):
    single_digit_primes = [2,3,5,7]
    length = len(single_digit_primes)
    prime_factors = []
    quotient = True
    # i=0
    while quotient is True:
        # for i in range(0,length+1):
    
        if number % single_digit_primes[0] == 0:
            prime_factors.append(single_digit_primes[0])
            number = int(number/single_digit_primes[0])
            # quotient = True
        elif number % single_digit_primes[1] == 0:
            prime_factors.append(single_digit_primes[1])
            number = int(number/single_digit_primes[1])
            # quotient = int(given_number/single_digit_primes[1])
        elif number % single_digit_primes[2] == 0:
            prime_factors.append(single_digit_primes[2])
            number = int(number/single_digit_primes[2])
            # quotient = int(given_number/single_digit_primes[2])
        elif number % single_digit_primes[3] == 0:
            prime_factors.append(single_digit_primes[3])
            number = int(number/single_digit_primes[3])
            # quotient = int(given_number/single_digit_primes[3])
        else :
            if number != 1:
                prime_factors.append(number)
                quotient = False
            else:
                quotient = False 
    print(prime_factors)


find_prime_factors(given_number)
  