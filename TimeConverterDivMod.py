#!/usr/bin/env python3

from sys import argv


def seconds_to_hours(seconds):
    
    m, s = divmod(abs(seconds), 60)
    h, m = divmod(m, 60)
    
    if seconds <= 0:
        full_time = f"-{h:02d}:{m:02d}:{s:02d}"

    else:
        full_time = f"{h:02d}:{m:02d}:{s:02d}"

    return {"full-time": full_time, 
            "h": h, 
            "m": m, 
            "s": s}


if __name__=='__main__':

    print("""     
                    {} second(s) -- input

                    {} hour(s)
                    {} minute(s)
                    {} second(s)

                    {} -- full time
                              """.format(argv[1],
                                         seconds_to_hours(int(argv[1]))["h"],
                                         seconds_to_hours(int(argv[1]))["m"], 
                                         seconds_to_hours(int(argv[1]))["s"],
                                         seconds_to_hours(int(argv[1]))["full-time"]
                                         )
          )
    
