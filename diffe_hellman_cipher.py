public_num_p = 23
public_num_g = 9

pvt_key_a = 4
pvt_key_b = 3

public_key_x = pow(public_num_g, pvt_key_a) % public_num_p
public_key_y = pow(public_num_g, pvt_key_b) % public_num_p

ka = pow(public_key_y, pvt_key_a) % public_num_p
kb = pow(public_key_x, pvt_key_b) % public_num_p

print(kb==ka)
