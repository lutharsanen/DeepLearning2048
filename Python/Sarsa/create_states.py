def get_all_states(length,base):
    states = []
    for i0 in range(length):
        print(i0)
        for i1 in range(length):
            for i2 in range(length):
                for i3 in range(length):
                    for i4 in range(length):
                        for i5 in range(length):
                            for i6 in range(length):
                                for i7 in range(length):
                                    for i8 in range(length):
                                        for i9 in range(length):
                                            for i10 in range(length):
                                                for i11 in range(length):
                                                    for i12 in range(length):
                                                        for i13 in range(length):
                                                            for i14 in range(length):
                                                                for i15 in range(length):
                                                                    states.append([base**i0 if i0!=0 else 0,base**i1 if i1!=0 else 0,base**i2 if i2!=0 else 0,base**i3 if i3!=0 else 0,base**i4 if i4!=0 else 0,base**i5 if i5!=0 else 0,base**i6 if i6!=0 else 0,base**i7 if i7!=0 else 0,base**i8 if i8!=0 else 0,base**i9 if i9!=0 else 0,base**i10 if i10!=0 else 0,base**i11 if i11!=0 else 0,base**i12 if i12!=0 else 0,base**i13 if i13!=0 else 0,base**i14 if i14!=0 else 0,base**i15 if i15!=0 else 0])
    return states


def get_all_states_light(length,base):
    states = []
    for i0 in range(length):
        for i1 in range(length):
            for i2 in range(length):
                for i3 in range(length):
                   states.append([base**i0 if i0 !=0 else 0,base**i1 if i1 !=0 else 0,base**i2 if i2!=0 else 0, base **i3 if i3!=0 else 0])
    return states

states = get_all_states(15,2)
f = open('states.txt', 'w')
f.write(str(states))