### ANSI color escape codes for use with AAWQ

## 0 prefaced codes are default colours
## 1 prefaced codes are bold colours
## 2 prefaced codes are light colours
## 3 prefaced codes are italic colours
## 4 prefaced codes are underlined colours
## 5, 6, and 7 have backgrounds.

##### Regular Colours #####
## black
sgr_0black = "\x1b[0;30;40m"
sgr_1black = "\x1b[1;30;40m"
sgr_2black = "\x1b[2;30;40m"
sgr_3black = "\x1b[3;30;40m"
sgr_4black = "\x1b[4;30;40m"
sgr_5black = "\x1b[5;30;40m"
sgr_6black = "\x1b[6;30;40m"
sgr_7black = "\x1b[7;30;40m"
## reds
sgr_0red = "\x1b[0;31;40m"
sgr_1red = "\x1b[1;31;40m"
sgr_2red = "\x1b[2;31;40m"
sgr_3red = "\x1b[3;31;40m"
sgr_4red = "\x1b[4;31;40m"
sgr_5red = "\x1b[5;31;40m"
sgr_6red = "\x1b[6;31;40m"
sgr_7red = "\x1b[7;31;40m"
## greens
sgr_0green = "\x1b[0;32;40m"
sgr_1green = "\x1b[1;32;40m"
sgr_2green = "\x1b[2;32;40m"
sgr_3green = "\x1b[3;32;40m"
sgr_4green = "\x1b[4;32;40m"
sgr_5green = "\x1b[5;32;40m"
sgr_6green = "\x1b[6;32;40m"
sgr_7green = "\x1b[7;32;40m"
## yellows
sgr_0yellow = "\x1b[0;33;40m"
sgr_1yellow = "\x1b[1;33;40m"
sgr_2yellow = "\x1b[2;33;40m"
sgr_3yellow = "\x1b[3;33;40m"
sgr_4yellow = "\x1b[4;33;40m"
sgr_5yellow = "\x1b[5;33;40m"
sgr_6yellow = "\x1b[6;33;40m"
sgr_7yellow = "\x1b[7;33;40m"
## blues
sgr_0blue = "\x1b[0;34;40m"
sgr_1blue = "\x1b[1;34;40m"
sgr_2blue = "\x1b[2;34;40m"
sgr_3blue = "\x1b[3;34;40m"
sgr_4blue = "\x1b[4;34;40m"
sgr_5blue = "\x1b[5;34;40m"
sgr_6blue = "\x1b[6;34;40m"
sgr_7blue = "\x1b[7;34;40m"
## magenta
sgr_0mag = "\x1b[0;35;40m"
sgr_1mag = "\x1b[1;35;40m"
sgr_2mag = "\x1b[2;35;40m"
sgr_3mag = "\x1b[3;35;40m"
sgr_4mag = "\x1b[4;35;40m"
sgr_5mag = "\x1b[5;35;40m"
sgr_6mag = "\x1b[6;35;40m"
sgr_7mag = "\x1b[7;35;40m"
## light green
sgr_0lgreen = "\x1b[0;36;40m"
sgr_1lgreen = "\x1b[1;36;40m"
sgr_2lgreen = "\x1b[2;36;40m"
sgr_3lgreen = "\x1b[3;36;40m"
sgr_4lgreen = "\x1b[4;36;40m"
sgr_5lgreen = "\x1b[5;36;40m"
sgr_6lgreen = "\x1b[6;36;40m"
sgr_7lgreen = "\x1b[7;36;40m"
## white
sgr_0white = "\x1b[0;37;40m"
sgr_1white = "\x1b[1;37;40m"
sgr_2white = "\x1b[2;37;40m"
sgr_3white = "\x1b[3;37;40m"
sgr_4white = "\x1b[4;37;40m"
sgr_5white = "\x1b[5;37;40m"
sgr_6white = "\x1b[6;37;40m"
sgr_7white = "\x1b[7;37;40m"

##### Reset #####
## Call Reset after every string calling a colour - otherwise color persists. ##
sgr_reset = "\x1b[0m"
