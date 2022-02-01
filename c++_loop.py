# #include <iostream>
# using namespace std;
 
# int main () {
#    // for loop execution
#    for( int a = 10; a < 20; a = a + 1 ) {
#       cout << "value of a: " << a << endl;
#    }
 
#    return 0;
# }

# value of a: 10
# value of a: 11
# value of a: 12
# value of a: 13

from re import A


LIMIT = 20
a = 10
while a < LIMIT:
    print("value of "+ str(a))
    a = a + 1