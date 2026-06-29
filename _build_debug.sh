#bin/bash

cd zephyr
west build -b nucleo_f767zi samples/basic/threads/ -- -DCMAKE_BUILD_TYPE=Debug