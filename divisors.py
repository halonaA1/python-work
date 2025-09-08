import sys

def get_joint_divisors(divisor1, divisor2, maximum):
   joint_divisors = []
   other = []

   for number in range(maximum +1):
       if number % divisor1 == 0 and number % divisor2 == 0:
           joint_divisors.append(number)
       else:
           other.append(number)

   return joint_divisors,other

def main():
  divisor1 = 2
  divisor2 = 12
  maximum =  50

  joint_divisors, other = get_joint_divisors(divisor1, divisor2, maximum)

  print(f"{joint_divisors = }")
  print()
  print(f"{other = }")

  return 0


if __name__ == "__main__":
    sys.exit(main())