#include <gmp.h>
#include <stdio.h>


int main() {
    mpz_t num1, num2, prod, target;

    mpz_init(num1);
    mpz_init(num2);
    mpz_init(prod);
    mpz_init(target);

    gmp_scanf("%Zd", target); // Read an integer into num1

		while (true) {
			if (mpz_com(prod, target)) {
				break;
			}
			if (mpz_com(prod, target) > 0) {
				mpz_tdiv_q(prod, prod, num1);
				mpz_add(num1, num1, 1);
			} else {
				mpz_mul(prod, prod, num1);
				mpz_sub(num1, num1, 1);
			}
		}

  	gmp_printf("%Zd %Zd", num1, num2);

    mpz_clear(num1);
    mpz_clear(num2);
    mpz_clear(prod);
    mpz_clear(target);

    return 0;
}

